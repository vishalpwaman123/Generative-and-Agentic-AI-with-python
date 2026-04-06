import os
import json
import requests
import anthropic
import subprocess
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel, Field
from typing import Union, Dict, Any

load_dotenv()

client = anthropic.Anthropic()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def run_command(cmd: str):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )

        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }

    except Exception as e:
        return {"error": str(e)}
    
def write_file(path: str, content: str):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return {"status": "success", "path": path}
    except Exception as e:
        return {"error": str(e)}

def get_weather_by_city(city: str) -> dict:
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            return {"error": data.get("message", "Unknown error")}

        return {
            "temperature": data["main"]["temp"],
            "feels_like":  data["main"]["feels_like"],
            "humidity":    data["main"]["humidity"],
            "weather":     data["weather"][0]["description"],
            "wind_speed":  data["wind"]["speed"],
        }
    except Exception as e:
        return {"error": str(e)}


AVAILABLE_TOOLS = {
    "get_weather_by_city": get_weather_by_city,
    "run_command": run_command,
    "write_file": write_file
}


SYSTEM_PROMPT = """
You are a step-by-step reasoning assistant.
Each response must contain EXACTLY ONE step as a JSON object (not an array).
Wait for the next user message before producing the next step.

Step types:
- START   : acknowledge the user query
- PROCESS : one reasoning thought
- TOOL    : call a tool (include "tool" and "input" fields)
- OUTPUT  : final answer (just say "Done." — weather is already shown to user)

Rules:
- Return ONLY a raw JSON object — no markdown, no ```json fences.
- One step per response, always.
- After a TOOL step, wait for the OBSERVER before continuing.

Available Tools:
- get_weather_by_city(city: str): Returns weather info for a city.
- run_command(cmd: str): Takes a system windows command as string and executes the command on user's system and returns the output from the command.
- write_file: Take a system to create file.

Format:
{"step": "START" | "PROCESS" | "TOOL" | "OUTPUT", "content": "...", "tool": "...", "input": "..."}

Example (one step per turn):

User: What is the weather in Delhi?
→ {"step": "START", "content": "User wants weather info for Delhi."}
→ {"step": "PROCESS", "content": "I should use get_weather_by_city tool for Delhi."}
→ {"step": "TOOL", "tool": "get_weather_by_city", "input": "delhi"}
→ {"step": "OBSERVER", "tool": "get_weather_by_city", "output": "{\"temperature\": 32.5, \"feels_like\": 30.8, \"humidity\": 24, \"weather\": \"clear sky\", \"wind_speed\": 5.7}"}
→ {"step": "OUTPUT", "content": "Great. I fetched Delhi weather information.\nTemperature is 32.5 °C.\nFeels like 30.8 °C.\nHumidity is 24%.\nWeather is clear sky.\nWind speed is 5.7 m/s."}

Instructions for project:
- First create folder using run_command
- Then create:
  - index.html
  - style.css
  - script.js
- write_file(path: str, content: str):
  - MUST always provide BOTH path and content
  - input must be JSON object like:
    {"path": "todo_application/index.html", "content": "<html>...</html>"}
- If file content is large:
  - Split into multiple TOOL steps
  - Use write_file for first chunk
  - Then append using write_file_append tool
- JS must support CRUD using localStorage

"""

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="the ID of the tool to call")
    # input: Optional[str] = Field(None, description="The input params for the tool")
    input: Optional[Union[str, Dict[str, Any]]] = None


def run_agent(user_query: str):
    try:
        conversation = [{"role": "user", "content": user_query}]

        while True:
            message = client.messages.parse(
                model="claude-haiku-4-5-20251001",
                max_tokens=4000,
                output_format=MyOutputFormat,
                system=SYSTEM_PROMPT,
                messages=conversation,
            )

            if not message.content:
                print("⚠️ Empty response from model. Stopping.")
                break

            parsed_result = message.content[0].parsed_output
            kind = parsed_result.step

            # Add model's step to conversation history
            conversation.append({
                "role": "assistant", 
                "content": parsed_result.model_dump_json()
            })

            if kind == "START":
                print("🔥 START   :", parsed_result.content)
                # Force next step
                conversation.append({
                    "role": "user",
                    "content": "Continue to next step."
                })

            elif kind == "PROCESS":
                print("⚙️  PROCESS :", parsed_result.content)
                # Force next step
                conversation.append({
                    "role": "user",
                    "content": "Continue to next step."
                })

            elif kind == "TOOL":
                tool_name = parsed_result.tool
                tool_input = parsed_result.input

                print(f"🛠️ TOOL: {tool_name} -> {tool_input}")

                # 🔥 AUTO FIX: convert string JSON → dict
                if isinstance(tool_input, str):
                    try:
                        tool_input = json.loads(tool_input)
                    except:
                        pass

                if tool_name in AVAILABLE_TOOLS:
                    if isinstance(tool_input, dict):
                        result = AVAILABLE_TOOLS[tool_name](**tool_input)
                    else:
                        result = AVAILABLE_TOOLS[tool_name](tool_input)
                else:
                    result = {"error": "Tool not found"}

                print("TOOL RESULT:", result)

                if isinstance(result, dict) and "error" in result:
                    print("Error:", result["error"])

                observer = {
                    "step": "OBSERVER",
                    "tool": tool_name,
                    "output": json.dumps(result)
                }

                conversation.append({
                    "role": "user",
                    "content": json.dumps(observer)
                })
            elif kind == "OUTPUT":
                print("✅ OUTPUT  :", parsed_result.content)
                break
    except Exception as e:
        print("Exception : ",e)

if __name__ == "__main__":
    while True:
        query = input("👉 ")
        run_agent(query)
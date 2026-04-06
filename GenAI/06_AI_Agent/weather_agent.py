import os
import json
import time

import requests
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_by_city(city: str) -> dict:
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=5)

        # Raise error for bad status codes (4xx, 5xx)
        response.raise_for_status()

        data = response.json()

        # Validate API response
        if data.get("cod") != 200:
            return {"error": data.get("message", "Unknown error")}

        # Format clean response
        weather_info = {
            "temperature": data.get("main", {}).get("temp"),
            "feels_like": data.get("main", {}).get("feels_like"),
            "humidity": data.get("main", {}).get("humidity"),
            "weather": data.get("weather", [{}])[0].get("description"),
            "wind_speed": data.get("wind", {}).get("speed")
        }
    
        return weather_info
    
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


SYSTEM_PROMPT = '''
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PROCESS and OUTPUT steps.
    You need to first PROCESS what needs to be done. The PROCESS can be multiple steps.
    Once you think enough PROCESS has beed done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    For every tool call wait for the observe step which is the output from the called tool.

    Follow steps:
    START → PROCESS → TOOL → OBSSERVER → PROCESS → OUTPUT
    
    Rules:
    - Strictly Follow the given JSON output format
    - If user not give input then take random Input.
    - Avoid infinite loop.
    - Do NOT wrap response in ```json or markdown. Return only raw JSON.
    - The sequence of steps is START (where user gives an input), 
      PLAN (That can be multiple times) and
      finally OUTPUT (which is going to the displayed to the user).

      Output JSON Format:
      [
      {"step": "START" | "PROCESS" | "OUTPUT" | "TOOL" | "OBSERVER" , "content": "string", "tool": "string", "input": "string"},
      {"step": "START" | "PROCESS" | "OUTPUT" | "TOOL" | "OBSERVER" , "content": "string", "tool": "string", "input": "string"},
      ...
      ]

      Available Tools : 
      - get_weather_by_city(city: str): Take city name as an input string and return the weather info abount the city.

      Example 1:
      [
        { "step": "START", "content": "What is the weather of Delhi?"},
        { "step": "PROCESS", "content": "Seems like user is interested in getting weather of delhi in India."},
        { "step": "PROCESS", "content": "Lets see if we have any available tool from the list of available tool."},
        { "step": "PROCESS", "content": "Great, we have get_weather_by_city tool available for this query."},
        { "step": "PROCESS", "content": "I need to call get_weather_by_city tool for delhi as input for city."},
        { "step": "TOOL", "tool": "get_weather_by_city", "input": "delhi"},
        { "step": "OBSERVER", "tool": "get_weather_by_city", "output": "{'temperature': 32.55, 'feels_like': 30.8, 'humidity': 24, 'weather': 'clear sky', 'wind_speed': 5.7}"},
        { "step": "PROCESS", "content": "Great, I got the weather info about delhi."},
        { "step": "OUTPUT", "content": "
                                        The current weather information of delhi
                                        Temperature : 32.55 °C"
                                        Feel like : 30.8 °C
                                        Humidity : 24 %
                                        Weather : Clear Sky
                                        Wind Speed : 5.7 m/s
                                        }
      ]
      
    '''

# ================= MAIN LOOP =================
conversation = []

user_input = {"role":"user", "content": input("👉 ")}

available_tools = {
    "get_weather_by_city" : get_weather_by_city
}

while True:

    message = client.messages.create(
    # model="claude-opus-4-6", #COSTLY
    model="claude-haiku-4-5-20251001", #CHEAPEST
    max_tokens=1000,
    system=SYSTEM_PROMPT, 
    messages=[user_input],
    )

    raw_result = message.content[0].text.strip()

    print(f"===========================================")
    print(f"raw_result : ", raw_result)

    # ✅ Parse JSON (list or single object)
    try:
        steps = json.loads(raw_result)
        if isinstance(steps, dict):
            steps = [steps]
    except json.JSONDecodeError:
        print("Invalid JSON. Retrying...")
        continue

    next_input_for_model = None

    print(f"===========================================")
    print(f"steps : ", steps)

    # ✅ Process each step
    for step in steps:
        step_type = step.get("step")

        if step_type == "START":
            print("🔥", step.get("content"))

        elif step_type == "PROCESS":
            print("⚙️ ", step.get("content"))

        elif step_type == "TOOL":
            tool_name = step.get("tool")
            tool_input = step.get("input")

            print(f"🛠️  Calling Tool: {tool_name}({tool_input})")

            if tool_name in available_tools:
                tool_result = available_tools[tool_name](tool_input)
                print("====== tool_result : ", tool_result)
            else:
                tool_result = {"error": "Tool not found"}

            # IMPORTANT: send tool result back to model
            observer_step = {
                "step": "OBSERVER",
                "tool": tool_name,
                "output": json.dumps(tool_result)
            }

            next_input_for_model = observer_step

        elif step_type == "OUTPUT":
            print("✅", step.get("content"))
            exit()   


    # # If tool was called → continue loop with OBSERVER
    # if next_input_for_model:
    #     conversation.append({
    #         "role": "assistant",
    #         "content": json.dumps(steps)
    #     })

    #     conversation.append({
    #         "role": "user",
    #         "content": json.dumps(next_input_for_model)
    #     })

    # else:
    #     # No tool used → break
    #     break

    # time.sleep(0.5) 
    exit()
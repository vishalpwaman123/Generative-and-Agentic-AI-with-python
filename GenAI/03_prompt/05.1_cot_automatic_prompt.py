#CHAIN OF THOUGHT PROMPTING

import json
import anthropic
from dotenv import load_dotenv
import time

load_dotenv()

client = anthropic.Anthropic()

SYSTEM_PROMPT = '''
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PROCESS and OUTPUT steps.
    You need to first PROCESS what needs to be done. The PROCESS can be multiple steps.
    Once you think enough PROCESS has beed done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - If user not give input then take random Input.
    - Avoid infinite loop.
    - Return ONLY one JSON object per response. Do not wrap in markdown.
    - Do NOT wrap response in ```json or markdown. Return only raw JSON.
    - The sequence of steps is START (where user gives an input), 
      PLAN (That can be multiple times) and
      finally OUTPUT (which is going to the displayed to the user).

      Output JSON Format:
      [
      {"step": "START" | "PROCESS" | "OUTPUT", "content": "string"},
      {"step": "START" | "PROCESS" | "OUTPUT", "content": "string"},
      ...
      ]

      Example:
      [
        {"step": "START", "content": "Hey, Can you solve 2 + 3 * 5 / 10"},
        {"step": "PROCESS", "content": "Seems like user is interested in maths problem"},
        { "step": "PROCESS", "content": "looking at the problem, we should solve this using BODMAS method"},
        { "step": "PROCESS", "content": "Yes, The BODMAS is correct thing to be done here"},
        { "step": "PROCESS", "content": "First we must multiple 3 * 5 which is 15"},
        { "step": "PROCESS", "content": "Now the new equation is 2 + 15 / 10"},
        { "step": "PROCESS", "content": "We must perform divide that is 15 / 10 = 1.5"},
        { "step": "PROCESS", "content": "Now the new equation is 2 + 1.5"},
        { "step": "PROCESS", "content": "Great, we have solved and finally left with 3.5 as answer"},
        { "step": "OUTPUT", "content": "3.5"}
      ]
    
    '''

user_input = {"role":"user", "content": input("👉  ")}

while True:

    message = client.messages.create(
    # model="claude-opus-4-6", #COSTLY
    model="claude-haiku-4-5-20251001", #CHEAPEST
    max_tokens=1000,
    system=SYSTEM_PROMPT, 
    messages=[user_input],
    )

    raw_result = message.content[0].text.strip()

    # ✅ Parse JSON (list or single object)
    try:
        parsed = json.loads(raw_result)
    except json.JSONDecodeError:
        print("Invalid JSON. Retrying...")
        continue

    # ✅ Normalize to list
    if isinstance(parsed, dict):
        parsed = [parsed]

    # ✅ Process each step
    for step_obj in parsed:
        step = step_obj.get("step")
        content = step_obj.get("content")

        if step == "START":
            print("🔥   ", content)

        elif step == "PROCESS":
            print("🧠   ", content)

        elif step == "OUTPUT":
            print("✅   ", content)
            exit()   # or break outer loop safely

        time.sleep(0.5)
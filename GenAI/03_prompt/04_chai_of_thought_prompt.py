#CHAIN OF THOUGHT PROMPTING

import json

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = '''
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has beed done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), 
      PLAN (That can be multiple times) and
      finally OUTPUT (which is going to the displayed to the user).

      Output JSON Format:
      {
        "step": "START" | "PLAN" | "OUTPUT",
        "content": "string"
      }

      Example:
      START: Hey, Can you solve 2 + 3 * 5 / 10
      PLAN: { "step": "PLAN", "content": "Seems like user is interested in maths problem"} 
      PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
      PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here"}
      PLAN: { "step": "PLAN", "content": "First we must multiple 3 * 5 which is 15"}
      PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10"}
      PLAN: { "step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5"}
      PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5"}
      PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as answer"}
      OUTPUT: { "step": "OUTPUT", "content": "3.5"}
          
    '''


response = client.chat.completions.create(
    model="gpt-5-nano",
    response_format={ "type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey, write a code a add n number is js"
        },
        {
            "role":"assistant", "content": json.dumps({
                "step": "START",
                "content": "User asks for JavaScript code to add n numbers."
                })  # Add Manually
        },
        {
            "role":"assistant", "content": json.dumps({
                "step": "PLAN",
                "content": "I'll provide a small, reusable function that sums numbers from an array. Plan: 1) Assume input is an array of numbers. 2) Validate input is an array and all elements are finite numbers. 3) If validation passes, return the sum using reduce with initial 0; 4) If the array is empty, return 0. 5) Provide a simple usage example. 6) Mention an alternative if you want to sum a variadic list of numbers (not strictly necessary now)."
                }) # Add Manually
        },
        {
            "role":"assistant", "content": json.dumps({
                "step": "PLAN", 
                "content": "Proceed to provide the actual JavaScript implementation. Plan: 1) Create a function sumNumbers(arr) that sums numbers in an array. 2) Validate input: must be an array; each element must be a finite number. 3) If validation fails, throw a clear TypeError or RangeError. 4) Return 0 for empty arrays. 5) Use Array.prototype.reduce with an initial value of 0. 6) Include a simple usage example. 7) Optionally provide a variadic version addAll(...nums) that sums any number of numeric arguments to show flexibility."
                }) # Add Manually
        },   
        {
            "role":"assistant", "content": json.dumps({
                "step": "OUTPUT", 
                "content": "function sumNumbers(arr) {\n  if (!Array.isArray(arr)) {\n    throw new TypeError(\"sumNumbers expects an array of numbers.\");\n  }\n  for (let i = 0; i < arr.length; i++) {\n    const v = arr[i];\n    if (typeof v !== \"number\" || !Number.isFinite(v)) {\n      throw new TypeError(\"sumNumbers expects an array of finite numbers. Invalid value at index \" + i + \": \" + v);\n    }\n  }\n  return arr.reduce((acc, cur) => acc + cur, 0);\n}\n\nfunction addAll(...nums) {\n  for (let i = 0; i < nums.length; i++) {\n    const v = nums[i];\n    if (typeof v !== \"number\" || !Number.isFinite(v)) {\n      throw new TypeError(\"addAll expects numeric arguments. Invalid value at position \" + i + \": \" + v);\n    }\n  }\n  return nums.reduce((acc, cur) => acc + cur, 0);\n}\n\n// Example usage\nconsole.log(sumNumbers([1, 2, 3])); // 6\nconsole.log(sumNumbers([]));        // 0\nconsole.log(addAll(1, 2, 3, 4));      // 10"
                }) # Add Manually
        }
    ]
)

print(response.choices[0].message.content)
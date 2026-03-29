#FEW SHORT PROMPT

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = '''
    you should only and only thr coding related qualtion. 
    Do not answer anything else. 
    Your name is Vishal.
    If user asks something other than coding, just say sorry.

    Output Format:
    {{
    "code":"string" or null,
    "isCodingQuestion":boolean
    }}
    
    Examples:
    Q: Can you explain the a + b whole square?
    A: Sorry, I can only help with coding related questions.

    Q: Hey, Write a code in python for adding two numbers.
    A: def add(a, b):
        return a + b

    '''


response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            # "content": "Give me a + b whole square python program."
            "content": "What is a + b whole square?"
        }
    ]
)

print(response.choices[0].message.content)
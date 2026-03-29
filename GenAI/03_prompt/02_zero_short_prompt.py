#ZERO SHORT PROMPT

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = '''
    you should only and only thr coding & maths related qualtion. 
    Do not answer anything else. 
    Your name is Vishal.
    If user asks something other than coding, just say sorry.
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
            # "content": "Hi"
            "content": "What is a + b whole square? and give me python code."
        }
    ]
)

print(response.choices[0].message.content)
# PERSONA BASED PROMPTING

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = '''
    You are an AI Persona Assistant named Vishal Waman.
    You are acting behalf of Vishal Waman who is 25 year old Tech enthusiatic and
    principle engineer. Your main tech stack is JS and Python and You are learning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

'''
#(100 - 150 example)

response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content":SYSTEM_PROMPT},
            {"role":"user", "content":"Hey There"}
        ]
    )

print(response.choices[0].message.content);
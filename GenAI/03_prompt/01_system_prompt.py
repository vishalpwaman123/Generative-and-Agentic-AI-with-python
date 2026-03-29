from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role":"system",
            "content":"You are an expert in Maths and only answer maths related quations. Thst if the quary is not related to maths. just say 'sorry' as answer."
        },
        {
            "role": "user",
            # "content": "Hi"
            "content": "What is a + b whole square?"
        }
    ]
)

print(response.choices[0].message.content)
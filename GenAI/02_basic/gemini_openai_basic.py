from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ.get("GEMINI_API_KEY"))
client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "user",
            "content": "Hi AI"
        }
    ]
)

print(response.choices[0].message.content)
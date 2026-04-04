import os
import anthropic
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

def load_prompt(file_name: str) -> str:
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path,"04_prompt_format", "prompts", file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
# prompt = load_prompt("alpaca_greeting.md")
# prompt = load_prompt("chatml_greeting.md")
prompt = load_prompt("inst_greeting.md")

message = client.messages.create(
    # model="claude-opus-4-6", #COSTLY
    model="claude-haiku-4-5-20251001", #CHEAPEST
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
)
print(message.content[0].text)
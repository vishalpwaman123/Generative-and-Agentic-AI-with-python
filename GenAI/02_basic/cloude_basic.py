import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    # model="claude-opus-4-6", #COSTLY
    model="claude-haiku-4-5-20251001", #CHEAPEST
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Hi Claude, Nice to meet you",
        }
    ],
)
print(message.content[0].text)
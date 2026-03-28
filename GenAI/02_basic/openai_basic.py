# Key : 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

from openai import OpenAI

client = OpenAI(
  api_key="OPENAI_SECRET_KEY"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="hi",
  store=True,
)

print(response.output_text);


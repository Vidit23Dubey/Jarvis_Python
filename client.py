from openai import OpenAI

client = OpenAI(
  api_key = "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",
)

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
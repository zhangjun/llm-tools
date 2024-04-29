model = "linkyllm-mixtral8x7b-15p1-sft-v1p3-int4"

from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:20000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=True,
  logprobs=True,
  top_logprobs=5,
)

for chunk in completion:
  print(chunk.choices[0])

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a skilled world class guitar player"},
    {"role": "user", "content": "Compose a sad song using basic chords"}
  ]
)

print(completion.choices[0].message)
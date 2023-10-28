import os
import openai
from dotenv import load_dotenv
# https://www.youtube.com/watch?v=GrX4WfT5FI4


load_dotenv()  # Load the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

"""
Request data

model
- ID of model to use.
- https://platform.openai.com/docs/models
- https://openai.com/pricing

messages
- A list of messages comprising the conversation so far.

temperature
- What sampling temperature to use, between 0 and 2.
- Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and 
  deterministic. for something technical where you want consise answers it's better to keep this value lower.

max_tokens
- The maximum number of tokens to generate in the chat completion.
"""

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Which NHL team plays in Pittsburgh?'},
    ],
    temperature=0.5,
    max_tokens=100
)

"""
Response data: chat completion object

https://platform.openai.com/docs/api-reference/chat/object

{
  "id": "chatcmpl-7sz349tSCvgxedXZSHbl7XSt6Eein",
  "object": "chat.completion",
  "created": 1693338738,          this is a unix timestamp in seconds
  "model": "gpt-4-0613",
  "choices": [                  can have multiple choices, but by default only 1 is returned unless you change this
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The NHL team that plays in Pittsburgh is the Pittsburgh Penguins."
      },
      "finish_reason": "stop"         #why did it stop, "stop" means the answer is just finished naturally, otherwise if not stop there might be errors
    }
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 12,
    "total_tokens": 36
  }
}
"""

print(response)
print()
print(response.choices[0].message)
print(response.choices[0].message.content)
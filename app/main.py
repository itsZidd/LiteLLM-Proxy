from litellm import completion
import os

os.environ['GROQ_API_KEY'] = ""
response = completion(
    model="groq/meta-llama/llama-4-scout-17b-16e-instruct", 
    messages=[
       {"role": "user", "content": "hello from litellm"}
   ],
    stream=True
)

for chunk in response:
    print(chunk)
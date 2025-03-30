import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# List of models to test
models = [
    "gpt-4o",
    "gpt-3.5-turbo-instruct",
    "davinci-002",
    "babbage-002",
    "o1",
    "o3-mini",
    "o1-mini"
]

# Prompt to send to each model
prompt = "What is the capital of France?"

# Iterate over each model and get a response
for model in models:
    try:
        if model in ["o1", "o3-mini", "o1-mini"]:
            # Use the completions endpoint with max_completion_tokens for o1 series models
            response = client.completions.create(
                model=model,
                prompt=prompt,
                max_completion_tokens=50
            )
            answer = response.choices[0].text.strip()
        elif model in ["gpt-3.5-turbo-instruct"]:
            # Use the completions endpoint with max_tokens for gpt-3.5-turbo-instruct
            response = client.completions.create(
                model=model,
                prompt=prompt,
                max_tokens=50
            )
            answer = response.choices[0].text.strip()
        elif model in ["davinci-002", "babbage-002"]:
            # Use the completions endpoint with max_tokens for davinci-002 and babbage-002
            response = client.completions.create(
                model=model,
                prompt=prompt,
                max_tokens=50
            )
            answer = response.choices[0].text.strip()
        else:
            # Use the chat completions endpoint with max_tokens for chat models
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=50
            )
            answer = response.choices[0].message.content.strip()

        print(f"Response from {model}: {answer}")

    except Exception as e:
        print(f"An error occurred with model {model}: {str(e)}")


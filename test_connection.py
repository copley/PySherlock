import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GPT_MODEL = "gpt-4-turbo-preview"

def test_gpt_api():
    """
    Sends a simple prompt to the GPT model to verify the API call.
    """
    prompt = "Hello, GPT! Please confirm that your API is working."
    try:
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=50
        )
        result = response.choices[0].message.content.strip()
        print("API call successful. Response:")
        print(result)
    except Exception as e:
        print(f"OpenAI API call failed: {e}")

if __name__ == "__main__":
    test_gpt_api()


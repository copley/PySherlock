import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables before using them
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# List of models to test
models_to_test = [
    "gpt-4.5-preview", "gpt-4o", "gpt-4o-audio-preview", "gpt-4o-realtime-preview",
    "gpt-4o-mini", "gpt-4o-mini-audio-preview", "gpt-4o-mini-realtime-preview",
    "o1", "o1-pro", "o3-mini", "o1-mini", "gpt-4o-mini-search-preview",
    "gpt-4o-search-preview", "computer-use-preview", "chatgpt-4o-latest",
    "gpt-4-turbo", "gpt-4", "gpt-4-32k", "gpt-3.5-turbo", "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-16k-0613", "davinci-002", "babbage-002",
    # Audio models might require specific endpoints
    "gpt-4o-audio-preview", "gpt-4o-mini-audio-preview", "gpt-4o-realtime-preview",
    "gpt-4o-mini-realtime-preview", "gpt-4o-mini-tts", "gpt-4o-transcribe",
    "gpt-4o-mini-transcribe", "whisper", "tts", "tts-hd",
    # Image generation
    "dall-e-3", "dall-e-2",
    # Embeddings
    "text-embedding-3-small", "text-embedding-3-large", "text-embedding-ada-002",
    # Moderation (typically free)
    "omni-moderation-latest", "text-moderation-latest"
]

# Lists to store results
working_models = []
failed_models = []

def test_model(model_name):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "Hello, test if working."}],
            temperature=0.2,
            max_tokens=10
        )
        print(f"Model {model_name}: WORKING")
        return True
    except Exception as e:
        print(f"Model {model_name}: FAILED ({e})")
        return False

if __name__ == "__main__":
    for model in models_to_test:
        print(f"Testing model: {model}")
        result = test_model(model)
        if result:
            working_models.append(model)
        else:
            failed_models.append(model)
        print("-" * 40)

    # Print a summary after all tests are complete
    print("\nSummary of test results:")
    print("Working endpoints:")
    for model in working_models:
        print(f"  - {model}")
    print(f"Total: {len(working_models)}\n")

    print("Not working endpoints:")
    for model in failed_models:
        print(f"  - {model}")
    print(f"Total: {len(failed_models)}")


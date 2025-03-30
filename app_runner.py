import os
import sys
import subprocess
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GPT_MODEL = "gpt-4-turbo-preview"

def run_python_app(app_path):
    """Run the Python application and capture stdout/stderr."""
    result = subprocess.run(
        [sys.executable, app_path],
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr

def bundle_python_files(directory, output_filename="output.txt"):
    """Combine all .py files from directory into one text file."""
    with open(output_filename, "w", encoding="utf-8") as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    outfile.write(f"# File: {filepath}\n{'#'*80}\n\n")
                    try:
                        with open(filepath, "r", encoding="utf-8") as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"\n# ERROR READING FILE: {e}\n")
                    outfile.write(f"\n{'#'*80}\n\n")
    print(f"Bundled code into {output_filename}")
    return output_filename

def analyze_error_with_gpt(error_message, bundled_code):
    """Send error and bundled code to GPT for analysis."""
    prompt = f"""
    My Python application encountered an error:
    ---
    {error_message}
    ---

    Here is my complete codebase:
    ---
    {bundled_code[:10000]}  # Limit to first 10,000 characters for efficiency
    ---

    Can you identify the problem and suggest how to fix it?
    """
    try:
        response = client.chat.completions.create(model=GPT_MODEL,
        messages=[
            {"role": "system", "content": "You're an expert Python debugger and coder."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1200)
        advice = response.choices[0].message.content.strip()
        return advice
    except Exception as e:
        return f"OpenAI API call failed: {e}"

def main():
    # Define your Python application entry point here:
    python_app_path = "your_code/script1.py"

    print(f"Running application: {python_app_path}")

    stdout, stderr = run_python_app(python_app_path)

    if stderr:
        print(f"\n❌ Application Error:\n{stderr}")

        # Bundle code for analysis
        bundled_code_path = bundle_python_files("your_code")

        with open(bundled_code_path, "r", encoding="utf-8") as file:
            bundled_code = file.read()

        print("\n🛠 Asking GPT-4-turbo-preview for help...")
        analysis = analyze_error_with_gpt(stderr, bundled_code)

        print("\n🔎 GPT Analysis & Recommendations:")
        print(analysis)
    else:
        print("\n✅ Application Output:")
        print(stdout)

if __name__ == "__main__":
    main()

# 🐍 PySherlock – GPT-powered Python Debugging Assistant

**PySherlock** is a powerful command-line tool designed to instantly identify and resolve Python errors by leveraging OpenAI's GPT-4-turbo-preview model. It simplifies the debugging process by analyzing your entire codebase alongside any runtime error messages, providing precise, AI-generated explanations and suggested solutions directly in your terminal.

## 🚀 Features

- **Instant Debugging:** Automatically captures Python errors and provides detailed insights.
- **GPT-4 Integration:** Utilizes OpenAI's GPT-4-turbo-preview for accurate and intelligent debugging.
- **Full Codebase Analysis:** Easily bundles your Python files into one readable format for comprehensive context.
- **Command-Line Simplicity:** Designed for ease of use directly from your terminal.

## ⚙️ Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/PySherlock.git
cd PySherlock
```

### Step 2: Set Up Environment

Create and activate a virtual environment (recommended):

```bash
python -m venv env
source env/bin/activate   # Linux/Mac
.\env\Scripts\activate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Configure OpenAI API Key

Create a `.env` file in the project root directory with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Obtain your API key at [OpenAI](https://platform.openai.com/api-keys).

## 🖥 Usage

Run your Python script through PySherlock:

```bash
python app_runner.py
```

PySherlock executes your code, captures any errors, and automatically sends the error along with your codebase to GPT-4 for analysis. The results are returned in clear, actionable advice directly in your terminal.

## 📂 Project Structure

```
PySherlock/
├── app_runner.py
├── .env
├── requirements.txt
└── your_code/
    ├── your_script.py
    └── additional_scripts.py
```

## 🎯 Example Output

When an error occurs, PySherlock provides:

```
❌ Application Error:
Traceback (most recent call last):
  File "your_script.py", line 3, in <module>
    print(undeclared_variable)
NameError: name 'undeclared_variable' is not defined

🛠 Asking GPT-4-turbo-preview for help...

🔎 GPT Analysis & Recommendations:
The error indicates you are trying to print a variable (`undeclared_variable`) that has not yet been defined or declared in your script. To fix this error, ensure the variable is initialized with a value before attempting to use it. For example:

```python
undeclared_variable = "Hello, world!"
print(undeclared_variable)
```
```

## 📜 License

MIT License

## ✨ Contributing

Contributions, issues, and feature requests are welcome!

- Fork the project
- Create a new branch (`git checkout -b feature/your-feature`)
- Commit your changes (`git commit -m 'Add some feature'`)
- Push to the branch (`git push origin feature/your-feature`)
- Open a pull request

---

**Happy Debugging!** 🔍🐍



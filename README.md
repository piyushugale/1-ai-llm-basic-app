# How to Connect to Groq and Run LLM Code

## 1. Sign Up for Groq Cloud
- Visit [https://console.groq.com/](https://console.groq.com/) and create a free account.

## 2. Get Your API Key
- After logging in, go to the "API Keys" section.
- Click "Create API Key" and copy your new key.

## 3. Install Required Python Package
Open your terminal and run:
```
pip install langchain_groq
```

## 4. Update Your Python Script
Replace `"YOUR_GROQ_API_KEY"` with your actual API key in the code below:

```python
API_KEY = "YOUR_GROQ_API_KEY"

from langchain_groq import ChatGroq
llm = ChatGroq(api_key = API_KEY, model="llama3-70b-8192")

response = llm.invoke("List Top 5 states in India")

print(f"content: {response.content}")
print(f"total_tokens: {response.usage_metadata['total_tokens']}")
print(f"id: {response.id}")
```

## 5. Run Your Script
Save your script (e.g., `llm-app-groq.py`) and run:
```
python llm-app-groq.py
```

## 6. Output
You will see the model's response, token usage, and request ID printed in your terminal.
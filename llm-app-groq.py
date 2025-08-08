API_KEY = "*********************"

from langchain_groq import ChatGroq

llm = ChatGroq(api_key = API_KEY, model="llama3-70b-8192")

response = llm.invoke("List Top 5 states in India  with capital and population")

print(f"content: {response.content}")
print(f"total_tokens: {response.usage_metadata['total_tokens']}")
print(f"id: {response.id}")

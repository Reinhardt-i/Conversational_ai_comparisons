import ollama 

response = ollama.generate(model="gemma2:2b", prompt="what is Gemma?")
print(response["response"])


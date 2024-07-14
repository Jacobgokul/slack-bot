import requests
import json

class CustomAgent:
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model
    
    def process_questions(self, text, question):
        answers = self.query_llm(text, question)
        return answers
    
    def query_llm(self, text, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": [{
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"Based on the following text, answer the question:\n\nText: {text}\n\nQuestion: {question}"
            }]
        }
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
            )

        if response.status_code == 200:
            response = response.json()
            response = response["choices"][0]["message"]["content"]
        else:
            error_detail = response.json().get("error", {}).get("message", "Unknown error")
            return error_detail

        return response

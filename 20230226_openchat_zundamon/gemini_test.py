import json
import requests
import os

api_key=os.getenv('GOOGLE_API_KEY')
my_question = "今まで「元気？」って何回訊かれましたか？"

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
params = {'key': api_key}
headers = {
    'Content-Type': 'application/json'
}
data = {
    "contents": [{
        "parts":[{
            "text": my_question}]}]}
response = requests.post(url, params=params, headers=headers, json=data)
data = response.json()
text = data['candidates'][0]['content']['parts'][0]['text']

print(my_question)
print(text)
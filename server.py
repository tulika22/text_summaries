from flask import Flask, request
import requests
import json
from openai import OpenAI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key = "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")

# headers = {
#     "accept": "application/json",
#     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMGZjOTJmMjMtNWY0Zi00ODM4LTg3OTMtYTM1ZGY2MDQzYWVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.gjJfE2jSeNtGw-hvnt_d8HWYMvi3z1Tqe1EJBVmwAeM"
# }

# url = "https://api.edenai.run/v2/text/summarize"
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMGZjOTJmMjMtNWY0Zi00ODM4LTg3OTMtYTM1ZGY2MDQzYWVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.gjJfE2jSeNtGw-hvnt_d8HWYMvi3z1Tqe1EJBVmwAeM

# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMGZjOTJmMjMtNWY0Zi00ODM4LTg3OTMtYTM1ZGY2MDQzYWVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.gjJfE2jSeNtGw-hvnt_d8HWYMvi3z1Tqe1EJBVmwAeM"
# }


@app.route('/summary', methods=['POST'])
def getSummary():

    persona = request.get_json()['persona']
    wordCount = request.get_json()['wordCount']
    text = request.get_json()['text']
    prompt = f"Create the summary of the following text: {text}"

    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {
                'role': 'system',
                'content': f'You are a {persona}'
            },
            {
                'role': 'user',
                'content': prompt
            },
            {
               'role': 'system',
               'content': f'Keep the summary length strictly around {wordCount} words.'
           }
        ]
    )

    return response.choices[0].message.content

#     payload = {
#     "response_as_dict": True,
#     "attributes_as_list": False,
#     "show_base_64": True,
#     "show_original_response": False,
#     "providers": ["openai"],
#     "text": request.get_json()['text'],
#     "messages": [
#         {"role": "system", "content": system_prompt},  # System prompt for persona
#         {"role": "user", "content": request.get_json()['text']},  # User-provided text
#         {'role': 'system','content': f'Keep the summary wordcount strictly {wordCount} words.'}
#     ]

# }
    # response = requests.post(url, json=payload, headers=headers)
    # data = response.json()
    # # print(data)
    # # print(response)
    # print(data["openai/gpt-4o"]["result"])

    # return data["openai/gpt-4o"]["result"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
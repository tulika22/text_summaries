from flask import Flask, request
import requests
import json
from openai import OpenAI
from flask_cors import CORS
import os 
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)



load_dotenv()

# Get the API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = OPENAI_API_KEY)

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
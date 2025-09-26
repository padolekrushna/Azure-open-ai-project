from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure Azure OpenAI
openai.api_type = "azure"
openai.api_base = "YOUR_ENDPOINT_HERE"  # e.g., https://xxxx.openai.azure.com/
openai.api_version = "2023-07-01-preview"
openai.api_key = "YOUR_API_KEY_HERE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    
    response = openai.ChatCompletion.create(
        engine="my-gpt-deployment",  # your deployment name
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize this: {text}"}
        ],
        max_tokens=100
    )
    
    summary = response['choices'][0]['message']['content'].strip()
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
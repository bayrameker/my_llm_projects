from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
import os

app = Flask(__name__)
CORS(app)

# Model ve tokenizer'ı yükleyin
model = GPT2LMHeadModel.from_pretrained('./models/code_model')
tokenizer = GPT2Tokenizer.from_pretrained('./models/code_model')

# Pipeline'ı oluşturun
nlp = pipeline('text-generation', model=model, tokenizer=tokenizer)

@app.route('/generate', methods=['POST'])
def generate_code():
    data = request.json
    prompt = data['prompt']
    results = nlp(prompt, max_length=100, num_return_sequences=1, truncation=True)
    generated_text = results[0]['generated_text']
    return jsonify({"generated_text": generated_text})

@app.route('/')
def serve_index():
    return send_from_directory('web', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('web', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

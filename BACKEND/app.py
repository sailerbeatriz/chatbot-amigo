from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

#API do Google Gemini
API_KEY = "AIzaSyBMuS9fKa-kWyaNilxCXGOxLQ410VMhdes"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Pega a mensagem do usuárioo
        user_message = request.json['message']
        
        # Gerar resposta usando Gemini
        response = model.generate_content(
            f"Responda como um assistente virtual amigável para idosos. "
            f"Seja claro, simples e paciente. Pergunta: {user_message}"
        )
        
        return jsonify({
            'response': response.text,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'response': 'Desculpe, tive um problema. Pode repetir?',
            'status': 'error'
        })

if __name__ == '__main__':
    app.run(debug=True)

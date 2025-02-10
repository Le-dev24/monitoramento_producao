from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo ao monitoramento de produção!"

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Olá, Mundo!'})
if __name__ == '__main__':
    app.run(debug=True, port=5001)
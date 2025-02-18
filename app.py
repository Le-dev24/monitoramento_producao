from flask import Flask, jsonify, request
app = Flask(__name__)

# Lista para armazenar os registros de produção (vem de monitoramento.py)
registros = []

# Função para registrar produção
def registrar_producao(turno, quantidade):
    registro = {'turno': turno, 'quantidade': quantidade}
    registros.append(registro)

    # Print os registros atuais no terminal após adicionar um novo registro
    print('Registros atuais: ', registros)

@app.route('/')
def home():
    return "Bem-vindo ao monitoramento de produção!"

# Rota para registrar a produção (via POST)
@app.route('/registrar_producao', methods=['POST'])
def api_registrar_producao():
    # Pegando os dados da requisiçao
    dados = request.get_json()
    turno = dados.get('turno')
    quantidade = dados.get('quantidade')

    # Chamando a função que já existe para registrar a produção
    registrar_producao(turno, quantidade)

    return jsonify({'message': 'Produção registrada com sucesso!', 'dados': dados})

# Rota para listar todos os registros
@app.route('/registros', methods=['GET'])
def listar_registros():
    return jsonify(registros)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
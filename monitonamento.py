import requests

# URL da API Flask onde os dados serão enviados
url = 'http://127.0.0.1:5001/registrar_producao'

# Sistema de Monitoramento de Produção - Versão 2

def registrar_producao ():
    """Função para registrar um novo dado de produção."""
    turno = input('Digite o turno (manha, tarde ou noite): ').strip().lower()
    quantidade = int(input('Digite a quantidade de itens produzidos: '))

    # Criando um dicionário com dados a serem enviados
    dados = {
        'turno': turno,
        'quantidade': quantidade
    }

    # Enviar dados via requisição POST para o servidor Flask
    response = requests.post(url, json=dados)

    # Verificando a resposta
    if response.status_code == 200:
        print('Registro salvo com sucesso!')
    else:
        print(f'Erro ao registrar a produção: {response.status_code}')

# Loop para continuar registrando até o usuário sair
while True:
    opcao = input('Deseja registar uma produção? (s/n): ') .strip().lower()

    if opcao == 's':
        registrar_producao()
    elif opcao == 'n':
        print('Saindo do sistema...')
        break
    else:
        print('Opção invalida! Digite "s" para sim e "n" para não.')


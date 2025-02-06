# Sistema de Monitoramento de Produção - Versão 1

# Lista para armazenar os registros de produção
registros = []

def registrar_producao ():
    """Função para registrar um novo dado de produção."""
    turno = input('Digite o turno (manhã, tarde ou noite): ').strip().lower()
    quantidade = int(input('Digite a quantidade de itens produzidos: '))

    # Criando um dicionário com dados
    registro = {'turno': turno, 'quantidade': quantidade}
    registros.append(registro)

    print('Registro salvo com sucesso!')

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


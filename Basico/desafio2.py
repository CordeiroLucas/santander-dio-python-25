LIMITE_SAQUE = 500

saldo = 0
depositos = []
saques_restantes = 3

DISPLAY = """
1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair
"""

EXIT_MESSAGE = 'Saindo do sistema...'

def depositar(valor):
    global saldo, depositos
    if valor <= 0:
        print('Valor inválido. O depósito deve ser maior que zero.')
        return -1
    
    saldo += valor
    depositos.append(valor)
    print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    
    return 0

def sacar(valor):
    global saldo, saques_restantes
    if saques_restantes <= 0:
        print('Número máximo de saques atingido.')
        return -1
    if valor <= 0:
        print('Valor inválido. O saque deve ser maior que zero.')
        return -1
    if valor > saldo:
        print('Saldo insuficiente para o saque.')
        return -1
    if valor > LIMITE_SAQUE:
        print(f'Saque excede o limite de R$ {LIMITE_SAQUE:.2f}.')
        return -1
    
    saldo -= valor
    saques_restantes -= 1
    print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
    
    return 0

def exibir_extrato():
    global depositos
    
    if not depositos:
        print('Nenhum depósito realizado.')
        return -1

    print('Extrato:')
    print(f'Saldo atual: R$ {saldo:.2f}')

    print('Depósitos realizados:')
    for dep in depositos:
        print(f'R$ {dep:.2f}')

    print(f'Saques restantes: {saques_restantes}')
    
    return 0

while True:
    print(DISPLAY)

    opcao = input('Escolha uma opção: ')

    if opcao == '0':
        print(EXIT_MESSAGE)
        break
    if opcao == '1':
        valor = float(input('Digite o valor do depósito: '))
        depositar(valor)
    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        sacar(valor)
    elif opcao == '3':
        exibir_extrato()
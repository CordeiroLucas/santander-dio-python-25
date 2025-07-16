LIMITE_SAQUE = 500

saldo = 0
depositos = []
saques_restantes = 3

while True:
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Extrato')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '0':
        print('Saindo do sistema...')
        break

    if opcao == '1':
        valor = float(input('Digite o valor do depósito: '))
        
        if valor <= 0:
            print('Valor inválido. O depósito deve ser maior que zero.')
            continue
        
        saldo += valor
        depositos.append(valor)
        
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')

    elif opcao == '2':
        if saques_restantes > 0:
            valor = float(input('Digite o valor do saque: '))
            if valor <= saldo and valor <= LIMITE_SAQUE:
                saldo -= valor
                saques_restantes -= 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Saque inválido. Verifique o saldo e o limite.')
        else:
            print('Número máximo de saques atingido.')

    elif opcao == '3':
        print('Extrato:')
        print(f'Saldo atual: R$ {saldo:.2f}')
        if depositos:
            print('Depósitos realizados:')
            for dep in depositos:
                print(f'R$ {dep:.2f}')
        else:
            print('Nenhum depósito realizado.')
        print(f'Saques restantes: {saques_restantes}')
    else:
        print('Opção inválida. Tente novamente.')
pagamentos = [12.344, 2.234, 524]

while True:
    print('0: sair')
    print('1: adicionar pagamento')
    print('2: remover pagamento')
    print('3: visualizar pagamentos atuais')

    opcoes = input('selecione: 0, 1, 2 ou 3')

    if opcoes == '1':
        pagamento = input('digite o pagamento')
        pagamentos.append(pagamentos)

    if opcoes == '2':
        print(pagamentos[0])
        pagamento = float(input('digite o valor a ser pago:'))
        if pagamento == pagamentos:
            print(f''' conta noo valor de {pagamentos.pop(0):.3f} efetuado''')
        else:
            print('valor insuficiente')    

    if opcoes == '3':
        print(f''' valore a serem cobrados: R$ {(pagamentos)}''')

    if opcoes == '0':
        break
            
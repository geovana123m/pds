pedidos = ['macarrão', 'strogonoff', 'bife']

while True:
    print('0: Sair')
    print('1: Adicionar pedido')
    print('2: Remover pedido')
    print('3: Visualizar pedidos atuais')

    opcoes = input('Selecione: 0, 1, 2 ou 3')

    if opcoes == '1':
        pedido = input('Digite o pedido')
        pedidos.append(pedidos)
    if opcoes =='2':
        print(pedidos.pop(0))
    if opcoes == '3':
        print(f'{len(pedidos)} - {pedidos}')
    if opcoes == '0':
        break
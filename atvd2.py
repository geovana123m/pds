atendimentos = ['idosos', 'deficientes', 'geral']

while True:
    print('0: Sair')
    print('1: Adicionar atendimento')
    print('2: Remover atendimento')
    print('3: Visualizar atendimentos atuais')

    opcoes = input('Selecione: 0, 1, 2 ou 3')

    if opcoes == '1':
        atendimento = input('Digite o serviço')
        atendimentos.append(atendimento)
    if opcoes =='2':
        print(atendimentos.pop(0))
    if opcoes == '3':
        print(f'{len(atendimentos)} - {atendimentos}')
    if opcoes == '0':
        break
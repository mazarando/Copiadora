print('Bem vindo(a) a Copiadora da Millenna Mazaro')
print('''
DIG - Digitalição
ICO - Impressão Colorida
IPB - Impressão Preto e Branco
FOT - Fotocópia
''')

total_pedido = 0

while True:

    servico = str(input('Entre com o Tipo de serviço desejado: ')).strip().upper()

    if servico not in  ['DIG', 'ICO', 'IPB', 'FOT']:
        print ('Resposta inválida. Tente Novamente.')
        continue

    if servico == 'DIG':
        preco = 1.10
    elif servico == 'ICO':
        preco = 1
    elif servico == 'IPB':
         preco = 0.40
    else: # servico == 'FOT'
         preco = 0.20

    try:
        num_paginas = int(input('Entre com as quantidades/números de páginas: '))
    except ValueError:
        print('Resposta inválida. Tente Novamente.')
        continue

    if num_paginas < 20: #Sem Desconto
        total = preco * num_paginas
    elif num_paginas >= 20 and num_paginas < 200: #Desconto de 15%
        total = preco * num_paginas * 0.85
    elif num_paginas >= 200 and num_paginas < 2000: #Desconto de 20%
        total = preco * num_paginas * 0.80
    elif num_paginas >= 2000 and num_paginas < 20000: #Desconto de 25%
        total = preco * num_paginas * 0.75
    else: # >= 20000
        print('Não aceitamos tantas páginas de uma vez.\n Por favor, entre com o número de páginas novamente.')
        continue

    total_pedido += total
    print(f'Total do pedido até agora: R${total_pedido:.2f}')

    while True:

        try:
            deseja = int(input('''Deseja adicionar algum serviço?
            1 - Encadernação simples - R$ 15.00
            2 - Encadernção Capa dura - R$ 40.00
            0 - Não desejo mais nada
            >> '''))
        except ValueError:
            print('Resposta inválida. Tente Novamente.')
            continue

        if deseja == 1:
            extra =  15
            total_pedido += extra
            print(f'Total: R${total_pedido:.2f} (serviço:{preco:.2f} * páginas:{num_paginas} + extra: {extra:.2f})')

        elif deseja == 2:
            extra = 40
            total_pedido += extra
            print(f'Total: R${total_pedido:.2f} (serviço:{preco:.2f} * páginas:{num_paginas} + extra: {extra:.2f})')

        elif deseja == 0:
            print(f'Total: R${total_pedido:.2f} (serviço:{preco:.2f} * páginas:{num_paginas})')

        else:
            print('Opção inválida. Tente Novamente.')
            continue
        break
    break
print('Fim do Programa.')

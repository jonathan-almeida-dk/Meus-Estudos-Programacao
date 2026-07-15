# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#     Depois disso, mostre:
#         A) Quantos números foram digitados.
#             B) A lista de valores, ordenada de forma decrescente.
#                 C) Se o valor 5 foi digitado e está ou não na lista.

lista=[]

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':  
        print('='*40)
        opções = int(input('Escolha uma das opções:' \
        '\n1 - Quantos números foram digitados' \
        '\n2 - Lista em ordem decrescente' \
        '\n3 - Existe o valor 5 na lista?' \
        '\n4 - Encerrar programa\nResposta: '))
        if opções == 1:
            print('='*40)
            print(f'Quantidade de números digitados foram {len(lista)}')
            break
        elif opções == 2:
            print('='*40)
            print(f'Itens da lista ordenada de forma decrescente {sorted(lista, reverse=True)}')
            break
        elif opções == 3:
            if 5 in lista:
                print(f'Sim, existe o valor 5 na lista e está na posição {lista.index(5) + 1}')
                break
        if opções == 4:
            break
print('='*40)
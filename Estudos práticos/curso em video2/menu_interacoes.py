import os
os.system('cls' if os.name == 'nt' else 'clear')
from time import sleep

opcoes = 0

print('Escolha 2 números:')
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
print('=-'*20)

while opcoes != 5:
    sleep(1)
    print('Selecione uma das opções abaixo:')
    opcoes = int(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\nResposta: '))
    print('=-'*20)

    if opcoes == 1:
        sleep(1)
        print(f'O resultado da soma entre {n1} e {n2} é de {n1+n2}.')
        print('=-'*20)
    elif opcoes == 2:
        sleep(1)
        print(f'O resultado da multiplicação entre {n1} e {n2} é de {n1*n2}.')
        print('=-'*20)
    elif opcoes == 3:
        if n1 > n2:
            sleep(1)
            print(f'O maior número é {n1}.')
            print('=-'*20)
        else:
            sleep(1)
            print(f'O maior número é {n2}.')
            print('=-'*20)
    elif opcoes == 4:
        sleep(1)
        print('Escolha 2 números:')
        n1 = int(input('1º Número: '))
        n2 = int(input('2º Número: '))
        print('=-'*20)
    elif opcoes == 5:
        sleep(1)
        print('Programa finalizado.')
    else:
        sleep(1)
        print('Opção inválida, tente novamente.')
        print('=-'*20)
print('Volte sempre!')
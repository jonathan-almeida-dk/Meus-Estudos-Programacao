import os 
clear = os.system('cls' if os.name == 'nt' else 'clear')
from time import sleep
from random import randint as rd


itens = ('Pedra', 'Papel', 'Tesoura') # cria uma lista e automaticamente a sequencia da lista é 1,2 e 3
pc = rd(0,3) # sempre que chama 'pc' o "computador" vai rodar um numero aleatorio entre 1 e 3

player = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)

print('-=' * 25)
print(f'O jogador escolheu {itens[player]} e o computador escolheu {itens[pc]}.')
print('-=' * 25)

if pc == 0: # COMPUTADOR JOGA PEDRA
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('JOGADOR VENCEU!')
    elif player == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1: # COMPUADOR JOGA PAPEL
    if player == 0:
        print('COMPUTADOR VENCEU!')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
    
elif pc == 2: # COMPUTADOR JOGA TESOURA
    if player == 0:
        print('JOGADOR VENCEU!')
    elif player == 1:
        print('COMPUTADOR VENCEU')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
    
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')








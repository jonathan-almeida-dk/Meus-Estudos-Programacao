# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

 
from random import randint

print(' JOGO DA ADIVINHA 2 '.center(40, '='))

computador = randint(0, 10)
palpite = 0
acertou = False

while not acertou:
    jogador = int(input('Pensei em um número, adivinhe: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez.')
        else:
            print('Menos... Tente outra vez.')
            
print(f'Você acertou. Foram necessários {palpite} palpites.')


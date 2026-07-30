# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
numeros = {}
from time import sleep
from random import randint
print('Valores Sorteados:')
for j in range(1,5):
    jogada = randint(1,6)
    print(f'Jogador {j} tirou {jogada} no dado.')
    numeros[f'Jogador {j}'] = jogada
numeros_ordenados = dict(sorted(numeros.items(),key=lambda item: item[1]))
print('-='*30)
print(' RANKING DOS JOGADORES '.center(60,'='))

for k, v in numeros_ordenados.items():
    print(f'{k} jogou {v}')
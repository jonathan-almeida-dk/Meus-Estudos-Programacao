# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6),}
ranking = []
print('Valores Sorteados:')
sleep(0.75)
for k, v in jogo.items():
    print(f'{k} jogou {v} no dado.')
    sleep(0.75)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(' RANKING DOS JOGADORES '.center(60,'='))
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

import os
clear = ('cls' if os.name == 'nt' else 'clear')

'''import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''

from random import choice
print('{:-^50}'.format('😋SORTEIO PRA QUEM EU VOU COMER O C*😋'))
a1 = str(input('Primeira pessoa: '))
a2 = str(input('Segunda pessoa: '))
a3 =str(input('Terceira pessoa: '))
a4 = str(input('Quarta pessoa: '))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O fudido(a) foi {}'.format(escolhido))
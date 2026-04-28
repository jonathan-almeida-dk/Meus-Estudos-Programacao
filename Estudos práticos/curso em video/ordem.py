import os
clear = os.system('cls' if os.name == 'nt' else 'clear')
clear
'''import random

print('{:-^60}'.format('📚 Ordem de quem apresentará o trabalho 📚'))
a1 = input('1° aluno: ')
a2 = input('2° aluno: ')
a3 = input('3° aluno: ')
a4 = input('4° aluno: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem será\n {}.'.format(lista))
'''
from random import shuffle
print('{:=^60}'.format('📚 Ordem de quem apresentará o trabalho 📚'))
a1 = input('1° aluno: ')
a2 = input('2° aluno: ')
a3 = input('3° aluno: ')
a4 = input('4° aluno: ')
lista = [a1,a2,a3,a4]
shuffle(lista)
print('A ordem será\n {}'.format(lista))



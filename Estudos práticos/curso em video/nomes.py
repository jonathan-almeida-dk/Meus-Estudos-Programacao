import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

clear

nome = str(input('Digite seu nome inteiro: ')).strip().split()

print('Muito prazer em te conhecer?')
print('Seu primeiro nome é {}.'.format(nome[0]))

print('Seu ultimo nome é {}.'.format(nome[-1]))
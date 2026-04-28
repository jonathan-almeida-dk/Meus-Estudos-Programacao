import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

clear
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculo é ',nome.upper())
print('Seu nome em minúsculo é ',nome.lower())

nm = ''.join(nome.split())
print('Seun ome tem ao todo {} letras.'.format(len(nm)))
#OU
#print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

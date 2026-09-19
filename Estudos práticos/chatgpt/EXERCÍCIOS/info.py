import os
os.system('cls' if os.name == 'nt' else 'clear')


profissao = input('Digite sua profissão: ').strip()
nome = input('Digite seu nome: ').strip()
idade = int(input('Digite sua idade: '))
print(f'Olá {nome}, você tem {idade} anos e é {profissao}.')


import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input(' Qual seu nome? ')
print(f'É um prazer te conhecer, {nome:✅^20}!', end = '\n\n')
print(f'É um prazer te conhecer, {nome:🍆^20}!', end = '\n\n')
print(f'É um prazer te conhecer, {nome:💦<20}!', end = '\n\n')
print(f'É um prazer te conhecer, {nome:🔞>20}!', end = '\n\n')
#explicando o uso do end para pular linhas ou não, por exemplo:
#o \n pula para a linha seguinte e se duas vezes aplicado, pula duas linhas;
#a persoanalização dos caracteres para o input "nome", pode ser movida para direita, esquerda ou centro.
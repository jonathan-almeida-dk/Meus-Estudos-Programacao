import os
os.system('cls' if os.name == 'nt' else 'clear')
from datetime import date
print("\033[34m-\033[m"*25)
print('\033[30mIDENTIFQUE SUA CATEGORIA\033[m')
print("\033[34m-\033[m"*25)
hoje = date.today() # ATRIBUI VALOR DA DATA DE HOJE PARA A VARIÁVEL "HOJE"
nascimento = int(input('Ano de nascimento: '))

idade_atual = hoje.year - nascimento #DESCOBRE A IDADE SUBTRAINDO O ANO ATUAL MENOS A DATA DE NASCIMENTO
print(f'A idade do atleta é \033[32m{idade_atual}\033[m anos!')

if idade_atual <= 9:
    print('A categoria do atleta é MIRIM!')
elif idade_atual <= 14:
    print('A categoria do atleta é INFANTIL!')
elif idade_atual <= 19:
    print('A cateogria do atleta é JUNIOR!')
elif idade_atual <= 25:
    print('A categoria do atleta é SÊNIOR!')
else:
    print('A categoria do atleta é MASTER!')

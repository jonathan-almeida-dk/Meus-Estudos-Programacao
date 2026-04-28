import os
from datetime import date
import sys #para encerrar o programa se for mulher
os.system('cls' if os.name == 'nt' else 'clear')

hoje = date.today()# ATRIBUI VALOR DA DATA DE HOJE PARA A VARIÁVEL "HOJE"
print('\033[32m-=\033[m' * 12)
print('\033[1:30:42mCONTADOR DE ALISTAMENTO\033[m')
print('\033[32m-=\033[m' * 12)

print('''[ 1 ] Feminino
[ 2 ] Masculino''')
sexo = int(input('Qual seu sexo?: '))

if sexo == 1:
    print('Você não precisa se alistar 💅')
    sys.exit() #encerra o programa

elif sexo == 2:
    ano = int(input('Ano de nascimento:'))
    idade_atual = hoje.year - ano #DESCOBRE A IDADE SUBTRAINDO O ANO ATUAL MENOS A DATA DE NASCIMENTO
    ano_alistamento = ano + 18 #ALTAMENTE INTUITIVO

    print(f'Quem nasceu em \033[32m{ano}\033[m tem \033[32m{idade_atual} anos\033[m em \033[32m{hoje.year}\033[m.')

    if idade_atual == 18:
        print('Está na HORA de se alistar!')
    elif idade_atual == 17: #fiz esse somente pra corrigir o português qaundo ele diz que falta 1 ANO invés de ANOS
        print(f'Você deverá se alistar daqui a \033[32m{ano_alistamento - hoje.year} ANO\033[m.')
    elif idade_atual > 18:
        print(f'Já deveria ter se alistado há \033[31m{hoje.year - ano_alistamento} ANOS\033[m.')
        print(f'Seu alistamento foi em \033[32m{ano_alistamento}\033[m caso já tenha se alistado.')
    elif idade_atual < 18:
        print(f'Você deverá se alistar daqui a \033[32m{ano_alistamento - hoje.year} ANOS\033[m.')
        print('Fica dbuenas meu homizinho 👶')
        print(f'Seu alistamento será em \033[32m{ano_alistamento}\033[m.')
else:
    sys.exit()
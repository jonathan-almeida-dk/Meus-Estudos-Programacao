import os
from datetime import date
os.system('cls' if os.name == 'nt' else 'clear')

ano = int(input('Digite o ano a ser analisado.\nOBS: Considere 0 como o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

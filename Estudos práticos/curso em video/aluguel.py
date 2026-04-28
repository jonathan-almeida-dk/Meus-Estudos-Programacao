import os
clear = os.system ('cls' if os.name == 'nt' else'clear')

dias = int(input('\33[1;33mPor quantos dias foi alugado?:\33[1;32m '))
km = float(input('\33[1;33mQuantos km foram rodados?:\33[1;32m '))
valor = dias*60 + km*0.15


print('\33[1;32mO total a pagar é de \033[4;31mR${:.2f}\033[m'.format(valor))

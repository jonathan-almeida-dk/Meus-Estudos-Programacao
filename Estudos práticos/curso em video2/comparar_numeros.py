import os
os.system('cls' if os.name == 'nt' else 'clear')

n1 = float(input('1° número: '))
n2 = float(input('2° número: '))

if n1 > n2:
    print('O primeiro número é o maior!')
elif n2 > n1:
    print('O segundo número é o maior!')
else:
    print('Os números são iguais!')
import os
os.system('cls')

n1 = float(input('Digite a nota: '))
n2 = float(input('Digite a 2ª nota: '))
n3 = float(input('Digite a 3ª nota: '))
m = (n1 + n2 + n3) /3
print('A média das notas é: {:.1f}.'.format(m))
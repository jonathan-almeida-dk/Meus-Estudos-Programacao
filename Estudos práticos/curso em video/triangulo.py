import os
os.system('cls' if os.name == 'nt' else 'clear')

seg1 = float(input('Digite um numero: '))
seg2 = float(input('Digite outro: '))
seg3 = float(input('Digite outro: '))

if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    print('Estes segmentos FORMAM UM TRIANGULO!')
else:
    print('Estes segmentos NÃO FORMAM UM TRIANGULO!')

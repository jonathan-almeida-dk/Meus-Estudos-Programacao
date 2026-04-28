import os
os.system('cls')

n = int(input('Um número:'))

print('{:=^60}'.format('CALCULANDO NÚMEROS'))
print('O dobro de {} é: {} \nO triplo é: {}\nA raiz quadrada é:{}'.format(n, n*2, n*3, n**(1/2)))
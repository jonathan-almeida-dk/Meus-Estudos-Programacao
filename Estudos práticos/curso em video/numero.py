import os
os.system('cls' if os.name == 'nt' else 'clear')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

#Verificando uem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor é {:.0f}'.format(menor))
print('O maior valor é {:.0f}'.format(maior))




'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))
'''
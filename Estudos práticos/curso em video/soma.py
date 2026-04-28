import os
clear = os.system('cls' if os.name == 'nt' else 'clear')
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2

#MÉTODO 1
#print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))

#MÉTODO 2
#print('A soma entre', n1, 'e', n2, 'é igual a',n1 + n2)

#MÉTODO 3
print('A soma total é {}'.format(s))

import os
os.system ('cls' if os.name == 'nt' else 'clear')

n = int(input('Digite um número: '))
antecessor = n - 1
sucessor = n + 1
print(' O numero {} tem como antecessor {} e sucessor {}'.format(n, antecessor, sucessor))

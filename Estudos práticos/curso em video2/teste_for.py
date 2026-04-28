import os
clear = os.system('cls' if os.name == 'nt' else 'clear')
'''
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')
'''
s = 1
for c in range(0,3):
    n = int(input('Digite um número: '))
    s+=n # ou seja s = s+n
print(f'A soma dos valores dá {s}!')
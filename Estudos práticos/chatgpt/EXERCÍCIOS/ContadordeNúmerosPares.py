
num = int(input('Digite um número: '))



# VERIFICAÇÃO DE NÚMEROS PARES
print(f'Esses são os números PARES dentro de {num}.')
for n in range(0, num+1, 2):
        print(n, end = ' ')

# VERIFICAÇÃO DE NÚMEROS ÍMPARES
print(f'\nEsses são os números ÍMPARES dentro de {num}.')
for n in range(1, num+1, 2):
        print(n, end = ' ')

# SOMA DOS PARES
tot = 0

for n in range(0,num+1):
    if n % 2 == 0:
        tot += n
print(f'\nA soma dos números pares é: {tot}')
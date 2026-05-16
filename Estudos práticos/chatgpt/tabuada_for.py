num = int(input('Digite um número e veja sua tabuada: '))

pares = 0
impares = 0

for t in range(0, 11):

    print(f'{num} x {t} = {num*t}')

    if t % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Resultados pares: {pares}')
print(f'Resultados ímpares: {impares}')

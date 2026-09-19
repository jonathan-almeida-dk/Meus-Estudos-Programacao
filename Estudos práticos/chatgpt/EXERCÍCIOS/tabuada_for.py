num = int(input('Digite um número e veja sua tabuada: '))

pares = 0
impares = 0
soma = 0
for t in range(0, 11):
    
    resultado = num * t 

    print(f'{num} x {t} = {resultado}')

    soma += resultado

    if resultado % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Soma dos resultados: {soma}')
print(f'Resultados pares: {pares}')
print(f'Resultados ímpares: {impares}')

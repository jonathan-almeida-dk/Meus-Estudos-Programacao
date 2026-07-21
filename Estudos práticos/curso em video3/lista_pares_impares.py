# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

numeros = [[],[]]
for c in range(1,8):
    valor = (int(input(f'Digite o {c}º número: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('='*45)
numeros[0].sort()
numeros[1].sort()
print(f'Todos os valores pares: {numeros[0]}')
print(f'Todos os valores ímpares: {numeros[1]}')
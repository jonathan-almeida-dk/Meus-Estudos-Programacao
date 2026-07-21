# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

lista =[]
pares = []
impares = []
for n in range(1,8):
    lista.append(int(input('Digite um número: ')))
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort()
lista.sort()
print(lista)
print(f'Lista de números pares {pares}')
print(f'Lista de números ímpares {impares}')
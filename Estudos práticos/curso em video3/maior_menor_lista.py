# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for n in range(0,5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
if max(lista) in lista:
    print(f'O maior valor foi {max(lista)} e está na posição {lista.index(max(lista))+1}')
if min(lista) in lista:
    print(f'O menor valor foi {min(lista)} e está na posição {lista.index(min(lista))+1}')

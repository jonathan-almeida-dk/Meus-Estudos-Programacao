# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for n in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0: # SE FOR O 1º NÚMERO DIGITADO E FOR IGUAL A 0:
        maior = menor = lista[n] # ELE SERÁ CONSIDERADO MAIOR E MENOR NÚMERO
    else:
        if lista[n] > maior: # se o numero da lista for maior que 'maior numero':
            maior = lista[n] # o 'maior numero' recebe o valor do numero da lista
        if lista[n] < menor: # se o numero da lista for menor que 'menor numero':
            menor = lista[n] # o 'menor numero' recebe o valor do numero da lista
print(lista)
print('='*40)
print(f'O maior valor foi {maior} e está na posição ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {menor} e está na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()
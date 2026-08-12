# Exercício Python 100: Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from random import randint as rd
from time import sleep as sl
números = []
def sorteia(lista):
    print(f'Os 5 números sorteados são: ', end='')
    for cont in range(0,5):
        n = rd(1,9)
        lista.append(n)
        print(n, end=' ', flush=True)
        sl(1)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma}')

sorteia(números)
somaPar(números)
# Exercício Python 100: Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from random import randint as rd
from time import sleep as sl
números = []
def sorteia():
    print(f'Os 5 números sorteados são: ', end='')
    for n in range(0,5):
        nums = rd(1,9)
        números.append(nums)
        print(nums, end=' ', flush=True)
        sl(1)

def somaPar():
    par = 0
    for i, n in enumerate(números):
        if n % 2 == 0:
            par += n
    print(f'\nSomando os valores pares de {números}, temos {par}')

sorteia()
somaPar()
# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe 
# esse módulo e use algumas dessas funções.

# Exercício Python 108: Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.

def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res

def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)
    return res

def dobro(preço=0):
    res = preço * 2
    return res

def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')
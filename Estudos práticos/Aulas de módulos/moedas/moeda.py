# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe 
# esse módulo e use algumas dessas funções.

# Exercício Python 108: Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.
import locale

def diminuir(preço, taxa):
    res = preço + (preço * taxa/100)
    return res

def aumentar(preço, taxa):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço):
    res = preço * 2
    return res

def metade(preço):
    res = preço / 2
    return res


def moeda(preço):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    res = locale.currency(preço, grouping=True, symbol=True)
    return res
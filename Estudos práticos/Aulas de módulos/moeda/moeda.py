# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe 
# esse módulo e use algumas dessas funções.

def diminuir(n):
    dez_porcento = n * 0.10
    diminuido = n - dez_porcento
    return diminuido

def aumentar(n):
    dez_porcento = n *0.10
    aumentado = n + dez_porcento
    return aumentado

def dobro(n):
    return 2 * n

def metade(n):
    return n / 2
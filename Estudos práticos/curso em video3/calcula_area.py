# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área():
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno de {larg}m x {comp}m é de {larg*comp}m².')
área()
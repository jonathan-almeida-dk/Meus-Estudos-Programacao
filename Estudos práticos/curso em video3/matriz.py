# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 
# e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

# 1. Inicializa a matriz 3x3 preenchida com zeros
matriz = [[0,0,0],[0,0,0],[0,0,0]]

# 2. Alimenta a matriz com dados do usuário
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)

# 3. Exibe a matriz formatada na tela
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()   # Quebra a linha ao fim de cada linha da matriz
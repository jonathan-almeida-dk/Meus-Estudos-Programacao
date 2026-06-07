# Pedir 5 números ao usuário.
# Mostrar:
# • Soma
# • Média

soma = 0

for n in range(1,6):                               # 'n' percorre a range de 1 à 6
    numero = int(input(f'Digite o {n}º número: ')) # pergunta 5 vezes um numero
    soma += numero                                 # variável soma recebe o valor dela mais o número dito pelo usuário cada vez que é perguntado ao mesmo
media = soma / 5                                   # divide o valor final entre soma e 5 e descobre a média
print(f'A média destes números é {media:.1f}.')

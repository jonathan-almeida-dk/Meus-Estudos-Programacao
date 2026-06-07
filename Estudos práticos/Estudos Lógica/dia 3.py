# Pedir 5 números ao usuário.
# Mostrar:
# • Soma
# • Média

soma = 0

for n in range(1,6):
    numero = int(input(f'Digite o {n}º número: '))
    soma += numero
media = soma / 5
print(f'A média destes números é {media:.1f}.')

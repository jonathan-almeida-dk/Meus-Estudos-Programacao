# Dia 6
# Revisão dos exercícios.
# Tente resolver novamente sem olhar.

# ===========================================

# Dia 1
# Problema:
# Mostrar os números de 1 a 10.

# for n in range(1,11):
#     print(n, end='')

# ===========================================

# Dia 2
# Mostrar apenas números pares de 1 a 20.

# for n in range(0,21,2):
#     print(n,end=' ')

# ===========================================

# Dia 3
# Pedir 5 números ao usuário.
# Mostrar:
# • Soma
# • Média

# cont = 0
# for n in range(5):
#     numero = int(input('Digite um número interio: '))
#     cont += numero
# print(f'A soma destes números é {cont}')
# print(f'A média destes números é {cont/5}')

# ===========================================

# Dia 4
# Descobrir o maior número de uma lista.

# lista = [2,4,10,55,100,0,6]
# maior = max(lista)
# print(maior)

# ===========================================

# Dia 5
# Contar quantas vogais existem numa palavra.

vogais = ['A','E','I','O','U']

palavra = input('Digite uma frase ou palavra: ').upper().strip()
for vogal in vogais:
    print(f'Na frase/palavra {palavra} possui ',palavra.count(vogal), f'{vogal}')


# ===========================================

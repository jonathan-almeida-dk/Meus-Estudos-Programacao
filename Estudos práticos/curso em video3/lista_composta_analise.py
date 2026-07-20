# Exercício Python 084: Faça um programa que leia nome e peso de 
# várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
#     B) Uma listagem com as pessoas mais pesadas.
#         C) Uma listagem com as pessoas mais leves.

info_totais = []
dados = []
mai = men = 0
while True:
    dados.append((input('Digite o nome: ')))
    dados.append((float(input('Digite o peso: '))))
    if len(info_totais) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    info_totais.append(dados[:])
    dados.clear()
    continuar = input('Deseja Continuar? [S/N]')
    if continuar in 'Nn':
        break
print('=-'*30)
print(f'Quantidade de Pessoas cadastradas: {len(info_totais)}')
print(f' O maior peso foi de {mai}Kg. Peso de ', end='')
for p in info_totais:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f' O menor peso foi de {men}Kg. Peso de ', end='')
for p in info_totais:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

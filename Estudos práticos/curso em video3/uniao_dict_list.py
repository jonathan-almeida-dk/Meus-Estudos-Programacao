# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: 
#     A) Quantas pessoas foram cadastradas 
#     B) A média de idade 
#     C) Uma lista com as mulheres 
#     D) Uma lista de pessoas com idade acima da média

pessoas = {}
galera = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = input('Nome: ')

    while True:
        pessoas['Sexo'] = input('Sexo [M/F]: ').upper()
        if pessoas['Sexo'] in 'MF':
            break
        print('Por favor, tente novamente [M/F]')
    pessoas['Idade'] = int(input('Idade: '))
    soma+= pessoas['Idade']
    galera.append(pessoas.copy())

    while True:
        continuar = input('Quer continuar? [S/N] ').upper()[0]
        if continuar in 'SN':
            break
        print('Por favor, tente novamente [S/N]')
    if continuar == 'N':
        break

print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastadas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('>> ENCERRADO <<')

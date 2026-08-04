# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: 
#     A) Quantas pessoas foram cadastradas 
#     B) A média de idade 
#     C) Uma lista com as mulheres 
#     D) Uma lista de pessoas com idade acima da média

pessoas = {}
while True:
    pessoas['Nome'] = input('Nome: ')

    while True:
        pessoas['Sexo'] = input('Sexo [M/F]: ').upper()
        if pessoas['Sexo'] not in 'MF':
            print('Por favor, tente novamente [M/F]')
        else:
            break
    pessoas['Idade'] = int(input('Idade: '))

    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar in 'N':
        break


print(pessoas)


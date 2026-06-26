# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

print('=' * 50)
print('Análise de Dados em Grupo'.center(50))
print('=' * 50)

maior = 0
homens = 0
mulheres_menos = 0

while True:
    idade = int(input('Digite a idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        
    # A) quantas pessoas tem mais de 18 anos.
    if idade > 18:
        maior += 1
        
    # B) quantos homens foram cadastrados.
    if sexo == 'M':
        homens += 1
        
    # C) quantas mulheres tem menos de 20 anos.
    if sexo == 'F' and idade < 20:
        mulheres_menos += 1
        
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        
    if continuar == 'N':
        break

print('=' * 50)
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homens} homens cadastrados.')
print(f'Existem {mulheres_menos} mulheres com menos de 20 anos.')

# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.
continuar = ''
print('='*50)
print('Análise de Dados em Grupo'.center(50))
print('='*50)
menor = 0
homens = 0
mulheres = 0
mulheres_menos = 0

while continuar != 'N':
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ')
    if idade < 18:
        menor+= 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos += 1
        mulheres += 1
    continuar = input('Deseja continuar? ').upper().strip()


# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.


while True:
    print('-='*20)
    num = int(input('Digite um número e veja sua tabuada: '))
    print('-='*20)
    if num < 0:
        break
    for contador in range(1,11):
        print(f'{num} X {contador} = {num*contador}')

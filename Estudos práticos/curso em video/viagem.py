import os
os.system('cls' if os.name == 'nt' else 'clear')

distancia = float(input('Qual a distância da viagem? '))

print('Você está prestes a começar uma viagem de {} Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
    print('E o valor da passagem é de R${:.2f}.'.format(preço))
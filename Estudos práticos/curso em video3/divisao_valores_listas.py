# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

números = []
pares = []
ímpares = []
while 0 not in números:
    num = (int(input('Digite um número: ')))
    números.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
print('Lista: ',números)
print('Pares: ',pares)
print('Ímpares: ',ímpares)
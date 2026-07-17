# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

números = []
pares = []
ímpares = []
while 0 not in números:
    números.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
for i, v in enumerate(números):
        if v % 2 == 0:
            pares.append(v)
        else:
            ímpares.append(v)
print('Lista: ',números)
print('Pares: ',pares)
print('Ímpares: ',ímpares)
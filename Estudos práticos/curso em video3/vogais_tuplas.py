# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Placa', 'Semaforo', 'Rua',
           'Pneu', 'Viaduto', 'Ponte',
           'Roda', 'Carro', 'Moto')
vogais = 'aeiouAEIOU'

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos', end=' --> ')
    for vogal in vogais:
            if vogal in palavra:
                print(f'{vogal.upper()}', end=' ')

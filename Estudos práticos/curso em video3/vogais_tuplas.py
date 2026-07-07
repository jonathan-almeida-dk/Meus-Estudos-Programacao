# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Placa', 'Semaforo', 'Rua',
           'Pneu', 'Viaduto', 'Ponte',
           'Roda', 'Carro', 'Moto')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
            if letra.lower() in 'aeiou':
                print(letra.upper(), end=' ')

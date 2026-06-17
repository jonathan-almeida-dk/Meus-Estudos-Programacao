''' Exercício Python 65:
    Crie um programa que leia vários números inteiros pelo teclado. 
    No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

soma = quantidade = media = maior = menor = 0
pergunta = 'S'

while pergunta == 'S':
    numeros = int(input('Digite um número: '))
    print('='*25)
    soma += numeros
    quantidade += 1
    if quantidade == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]
    print('='*25)

media = soma / quantidade
print('='*25)
print(f'Você digitou {quantidade} números.')
print('='*25)
print(f'Maior número é * {maior} *.')
print('='*25)
print(f'Menor número é * {menor} *.')
print('='*25)
print(f'A média dos números é * {media} *.')
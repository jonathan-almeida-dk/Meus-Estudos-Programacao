# Exercício Python 079: Crie um programa onde o usuário possa
# digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('='*50)
print('PROGRAMA DE LISTAGEM NUMÉRICA'.center(50))
print('='*50)

numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado.')
    else:
        print('Valor repetido! Tente novamente.')
    perg = input('Quer digitar outro número? ').strip()[0].upper()
    if perg in 'Nn':
        break
print('='*50)

numeros.sort()
print(f'Os números digitados foram {numeros}.')
        



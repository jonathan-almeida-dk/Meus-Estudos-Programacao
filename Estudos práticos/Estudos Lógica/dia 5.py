# Dia 5
# Contar quantas vogais existem numa palavra.

palavra = input('Digite uma palavra ou frase: ').upper().strip()

vogais = ['A', 'E', 'I', 'O', 'U']

for vogal in vogais:
    quantidade = palavra.count(vogal)
    print(f'A frase possui {quantidade} letras {vogal}')


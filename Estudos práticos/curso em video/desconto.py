import os
clear = os.system ('cls' if os.name == 'nt' else 'clear')

valor = float(input( 'Valor do produto? R$ '))
novo = valor - (valor / 100 * 5)

print(f'O produto que custava R${valor:.2f}, com desconto de 5%, agora custa R${novo:.2f}.')
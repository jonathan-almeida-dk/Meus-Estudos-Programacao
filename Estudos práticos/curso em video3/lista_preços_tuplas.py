# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Arroz', 14.96, 
            'Feijão', 20.50, 
            'Mostarda', 5.98,
            'Macarrão', 3.95, 
            'Refrigerante', 9.98, 
            'Maionese', 11.95)
print('-='*20)
print('Listagens de Produtos'.center(40))
print('-='*20)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-='*20)
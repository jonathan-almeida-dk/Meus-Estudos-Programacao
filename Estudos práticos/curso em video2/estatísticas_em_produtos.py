print('-'*30)
print('Lojinha do Seu LEÔncio'.center(30))
print('-'*30)

preço = valor_total = produto_mil_reais = menor = cont = 0
barato = ''
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
    cont += 1
    valor_total += preço

    if preço >= 1000:
        produto_mil_reais += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0 ]
    if continuar == 'N':
        break

print(f'O total da compra é de R${valor_total:.2f}')
print(f'Temos {produto_mil_reais} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}.')
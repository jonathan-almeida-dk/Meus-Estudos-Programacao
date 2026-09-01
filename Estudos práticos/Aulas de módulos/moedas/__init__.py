import moeda

num = float(input('Digite o preço: '))
print(f'A metade de R${num:.2f} é R${moeda.metade(num):.2f}')
print(f'O dobro de R${num:.2f} é R${moeda.dobro(num):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num,10):.2f}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(num,10):.2f}')

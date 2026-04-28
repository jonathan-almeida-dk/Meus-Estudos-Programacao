import os
os.system('cls' if os.name == 'nt' else 'clear')

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))

prestacao = casa / (anos * 12)
minimo = salario * 0.30

print(f'\nA casa do valor de R${casa:.2f} em {anos} anos,', end=' ')
print(f'as prestações serão de R${prestacao:.2f}')

if prestacao <= minimo:
    print('\033[32mEmpréstimo CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')
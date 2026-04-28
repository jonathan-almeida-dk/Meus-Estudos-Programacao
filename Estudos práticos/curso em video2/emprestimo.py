import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('-=' * 10)
print('ANALISADOR DE EMPRÉSTIMOS')
print('-=' * 10)

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: '))
anos = int(input('Em quantos anos pretende pagar?: '))

prestacao = casa / (anos * 12)     #GERA O VALOR DE CADA PRESTAÇÃO
minimo_30 = salario * 0.30         #DEFINE QUE NÃO PODE PASSAR DE 30% DO SALARIO
juros = (prestacao / 100) * 5      #CALCULA A PORCENTAGEM DE JUROS DA PARCELA(NESSE CASO 5% DO VALOR DA PRESTAÇÃO)

print(f'\nPara pagar uma casa de R${casa:.2f} em {anos} anos,', end =' ')
print(f'a prestação será de R${prestacao + juros:.2f}.')
if prestacao + juros <= minimo_30: #AQUI EU SOMO O VALOR DOS JUROS MAIS A PRESTAÇÃO E DELIMITO 30% DO SALÁRIO
    print('\033[32mEmpréstimo CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')





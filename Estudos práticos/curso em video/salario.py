import os
os.system('cls' if os.name == 'nt' else 'clear')

salario = float(input('Qual o seu salário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 /100)
print('Seu novo salário é de R${:.2f}.'.format(novo))






'''
salario = float(input('Qual o seu salário? R$'))
novo = salario + (salario * 15 / 100)
if salario > 1250:
    novo = salario + (salario * 10 / 100)

print('Seu salário passa a ser R${:.2f}.'.format(novo))
'''
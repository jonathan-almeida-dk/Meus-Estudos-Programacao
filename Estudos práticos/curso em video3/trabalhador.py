# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e 
# carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o 
# ano de contratação e o salário. Calcule e acrescente, além da idade, com 
# quantos anos a pessoa vai se aposentar.
from datetime import date

trabalhador = {'Nome ' : input('Nome: '),
               'Data de Nascimento' : int(input('Ano de Nascimento: ')),
               'CTPS' : int(input('Carteira de Trabalho (0 não tem): '))
               }
idade = date.today().year - trabalhador["Data de Nascimento"]
trabalhador["Idade: "] = idade
if trabalhador["CTPS"] != 0:
    trabalhador["Contratação"] = int(input('Ano de contratação: '))
    trabalhador["Salário"] = float(input('Salário: R$ '))
    aposentado = trabalhador["Contratação"] + 35
    print('-='*30)
    trabalhador["Aposentadoria"] = aposentado

for k, v in trabalhador.items():
    print(f'{k}: {v}.')
# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto 
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date
def voto(ano=0):
    nasc = int(input('Em que ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade <= 15:
        print(f'Com {idade} anos: NÃO VOTA!')
    elif 16 <= idade <= 17:
        print(f'Com {idade} anos: É OPCIONAL!')
    elif 18 <= idade <= 69:
        print(f'Com {idade} anos: É OBRIGATÓRIO!')
    else:
        print(f'Com {idade} anos: É OPCIONAL!')




# Programa Principal
voto()
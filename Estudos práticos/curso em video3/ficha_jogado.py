# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog = '<desconhecido>', gols = '0'):
    jog = str(input('Nome do jogador: '))
    gols = str(input('Número de gols: '))
    if jog in '<desconhecido>':
        jog = '<desconhecido>'
    if gols in '':
        gols = 0
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato')

# Programa Principal
ficha(gols=0)

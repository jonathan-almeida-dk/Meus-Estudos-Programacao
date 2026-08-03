# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

info = {}
gols = []
totgols = 0
info['Nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {info["Nome"]} jogou? '))
while True:
    if partidas != 0:
        for c in range(1,partidas+1):
            gol = (int(input(f'Quantos gols ele fez na {c}ª partida? ')))
            gols.append(gol)
            totgols += gol
        info['Gols'] = gols
        break
info['Total de Gols'] = totgols


print(info)
# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

info = {}
gols = []
totgols = 0
nome = info['Nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {nome} jogou? '))
while True:
    if partidas != 0:
        for c in range(1,partidas+1):
            info['Gols'] = (int(input(f'Quantos gols na {c}º partida? ')))
            totgols += info["Gols"] 
        break
print(info)
print('Gols: ',info["Gols"])
print('Total de gols: ',totgols)
        
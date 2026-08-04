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
        for c in range(0,partidas):
            gol = (int(input(f'Quantos gols ele fez na {c+1}ª partida? ')))
            gols.append(gol)
            totgols += gol
        info['Gols'] = gols
        break
info['Total de Gols'] = totgols
print('-='*30)

# DEMOSTRAÇÕES:
print(info)
print('-='*30)
for k, v in info.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)

print(f'O jogador {info["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(info['Gols']):
    print(f'    Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {info['Total de Gols']} gols.')

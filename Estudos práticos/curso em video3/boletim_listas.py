# Exercício Python 089: Crie um programa que leia nome e duas notas de vários
# alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

info_notas = []
dados = []
while True:
    nome = dados.append(input('Digite o nome: '))
    n1 = dados.append(float(input(f'Digite a 1ª nota: ')))
    n2 = dados.append(float(input(f'Digite a 2ª nota: ')))
    info_notas.append(dados[:])
    dados.clear()
    resp = input('Quer continuar?: ')
    if resp in 'Nn':
        print('-'*30)
        print(' BOLETIM '.center(30))
        print('-'*30)
        for n in range(1):
            print('Aluno: ',info_notas[0][0])
            media = (info_notas[0][1] + info_notas[0][2]) / 2
            print('Média: ',media)
        break

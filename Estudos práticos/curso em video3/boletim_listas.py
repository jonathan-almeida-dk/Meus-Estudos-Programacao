# Exercício Python 089: Crie um programa que leia nome e duas notas de vários
# alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = []
while True:
    nome = (input('Digite o nome: '))
    n1 = (float(input(f'Digite a 1ª nota: ')))
    n2 = (float(input(f'Digite a 2ª nota: ')))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1,n2], media])
    resp = input('Quer continuar?: ')
    if resp in 'Nn':
        break

print('-='*30)
print(f'{"N°":<4}{'Nome':<10}{'Média':>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    
while True:
    
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe:)'))
    if opc == 999:
        print('FINZALIZANDO...')
        break
    
    if opc<= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}]')
print('Volte sempre!')

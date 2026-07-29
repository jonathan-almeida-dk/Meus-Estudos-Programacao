# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
alunos = {}
alunos['Nome'] = input('Nome: ')
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
if alunos["Média"] >= 8:
    alunos['Situação'] = 'Aprovado'
elif 6 <= alunos["Média"] <8:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
print('-='*30)
for k, v in alunos.items():
    print(f' - {k} é igual a {v}')
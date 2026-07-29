# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
alunos = {}

alunos['Nome'] = input('Nome: ')
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
print('-='*30)
print(f'O nome é igual a {alunos["Nome"]}')
print(f'A média é igual a {alunos["Média"]}')
if alunos["Média"] >= 8:
    print(f'A situação é igual a Aprovado.')
elif alunos["Média"] >=6:
    print(f'A situação é igual a Recuperação.')
elif alunos["Média"] < 6:
    print(f'A situação é igual a Reprovado')
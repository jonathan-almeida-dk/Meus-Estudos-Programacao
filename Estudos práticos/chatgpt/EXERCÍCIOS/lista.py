
# # Exercício 1 — Lista de frutas 🍎
# lista_frutas = ['Banana', 'Maçã', 'Pera', 'Morango', 'Uva']
# print(lista_frutas)
# print(lista_frutas[0])
# print(lista_frutas[-1])




# # Exercício 2 — Adicionando nomes 👾
# nomes = []

# for n in range(5):
#     nome = input('Digite um nome: ')
#     nomes.append(nome)
# print(nomes)



# # Exercício 3 — Soma de números 🔥
# numeros = []

# for n in range(5):
#     numero = int(input('Digite um numero: '))
#     numeros.append(numero)

# soma = sum(numeros)
# print(numeros)
# print(soma)


# Exercício 4 — Maior e menor número 🚀
# numeros = []
# for n in range(5):
#     numero = int(input('Digite um numero: '))
#     numeros.append(numero)
# print('O maior numero é: ',max(numeros))
# print('O menor numero é: ',min(numeros))

# Exercício 5 — Sistema simples de alunos 🧑‍💻
from sys import exit

lista_alunos = []

def adicionar_alunos():
    aluno = input('Digite o nome do aluno: ')
    lista_alunos.append(aluno)

def mostrar_alunos():
    lista_alunos.sort()
    print('\n' .join(lista_alunos))

def remover_alunos():
    aluno_removido = input('Digite o nome do aluno: ')
    if aluno_removido in lista_alunos:
        lista_alunos.remove(aluno_removido)
    else:
        print('Aluno não encontrado.')

def sair_sistema():
    print('Sistema Encerrado.')
    exit()
        


while True:
    print('\n======= Sistema de Alunos =======')
    print('\n======= OPÇÕES =======')
    print('''    1 - Adicionar 
    2 - Mostrar 
    3 - Remover 
    4 - Sair''')
    try:
        opcao = int(input('\nDigite uma das opções: '))
        if opcao == 1:
            adicionar_alunos()
        elif opcao == 2:
            mostrar_alunos()
        elif opcao == 3:
            remover_alunos()
        elif opcao == 4:
            sair_sistema()
        else:
            print('Opção inválida! Tente novamente.')
            continue

    except ValueError:
        print('Digite apenas números! Tente novamente.')





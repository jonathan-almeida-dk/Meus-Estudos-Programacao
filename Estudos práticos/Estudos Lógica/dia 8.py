# Dia 8
# Cadastro simples de nomes.
# Menu:
# 1 - Adicionar
# 2 - Mostrar
# 3 - Sair 

lista_nomes = []
opcoes = 0

print('=' * 40)
print('MENU PRINCIPAL'.center(40))
print('=' * 40)
print(' CADASTROS DE NOMES '.center(40, '-'))
print('1 - Adicionar\n' \
'2 - Mostrar\n' \
'3 - Sair')
print('=-'*20)
while opcoes != 3:
    opcoes = int(input('Escolha uma das opções: '))
    if opcoes == 1:
        nomes = input('Adicione um nome: ')
        lista_nomes.append(nomes)
        print('=-'*20)
    elif opcoes == 2:
        print(lista_nomes)
        print('=-'*20)
    elif opcoes == 3:
        print('Programa finalizado.')
        print('=-'*20)
    else:
        print('Opção inválida, tente novamente.')
        print('=-'*20)
    
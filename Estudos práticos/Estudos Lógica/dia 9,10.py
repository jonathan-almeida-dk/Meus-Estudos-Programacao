# Dia 9
# Adicionar remoção de nomes.

# Dia 10
# Buscar um nome específico.

from time import sleep
lista_nomes = []
opcoes = 0

while opcoes != 4:
    print('=' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('=' * 40)
    sleep(1.5)
    print(' CADASTROS DE NOMES '.center(40, '-'))
    print('1 - Adicionar\n' \
    '2 - Mostrar\n' \
    '3 - Remover\n' \
    '4 - Sair')
    print('=-'*20)
    sleep(1.5)
    opcoes = int(input('Escolha uma das opções: '))
    print('=-'*20)
    sleep(1.5)
    if opcoes == 1:
        sleep(1.5)
        nomes = input('Adicione um nome: ')
        lista_nomes.append(nomes)
        print('NOME ADICIONADO COM SUCESSO.')
        print('=-'*20)
        sleep(1.5)
    elif opcoes == 2:
        print('Lista de nomes'.center(40))
        print(lista_nomes)
        print('=-'*20)
        sleep(1.5)
    elif opcoes == 3:
        remover = input('Qual nome você desja remover?: ')
        lista_nomes.remove(remover)
        print('NOME REMOVIDO COM SUCESSO')
        print('=-'*20)
        sleep(1.5)
    elif opcoes == 4:
        print('Programa finalizado.')
        print('=-'*20)
        sleep(1.5)
    else:
        print('Opção inválida, tente novamente.')
        print('=-'*20)
        sleep(1.5)
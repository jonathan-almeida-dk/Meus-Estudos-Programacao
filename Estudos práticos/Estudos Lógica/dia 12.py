# Dia 12
# Salvar em arquivo TXT.

from time import sleep
lista_nomes = []
opcoes = 0
save_nomes = lista_nomes

while opcoes != 6:
    print('=' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('=' * 40)
    sleep(1)

    print(' CADASTROS DE NOMES '.center(40, '-'))
    print('1 - Adicionar\n' \
    '2 - Mostrar\n' \
    '3 - Remover\n' \
    '4 - Ordenar\n' \
    '5 - Salvar\n' \
    '6 - Sair')
    print('=-'*20)
    sleep(1)

    opcoes = int(input('Escolha uma das opções: '))
    print('=-'*20)
    sleep(1)

    if opcoes == 1:
        sleep(1)
        nomes = input('Adicione um nome: ')
        lista_nomes.append(nomes)
        print('NOME ADICIONADO COM SUCESSO.')
        print('=-'*20)
        sleep(1)

    elif opcoes == 2:
        print('Lista de nomes'.center(40))
        print(lista_nomes)
        print('=-'*20)
        sleep(1)

    elif opcoes == 3:
        remover = input('Qual nome você desja remover?: ')
        lista_nomes.remove(remover)
        print('NOME REMOVIDO COM SUCESSO')
        print('=-'*20)
        sleep(1)

    elif opcoes == 4:
        lista_nomes.sort()
        print('Lista em Ordem Alfabética'.center(40))
        print(lista_nomes)
        sleep(1)

    elif opcoes == 5:
        with open('listanomes.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(str(save_nomes))

    elif opcoes == 6:
        print('Programa finalizado.')
        print('=-'*20)
        sleep(1)

    else:
        print('Opção inválida, tente novamente.')
        print('=-'*20)
        sleep(1)
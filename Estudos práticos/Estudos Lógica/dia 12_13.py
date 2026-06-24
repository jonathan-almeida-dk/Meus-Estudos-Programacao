# Dia 12
# Salvar em arquivo TXT.
# Dia 13
# Ler os dados do TXT ao iniciar.

from time import sleep
lista_nomes = []
opcoes = 0
save_nomes = lista_nomes

def ler_arquivo():
    try:
        with open('listanomes.txt','r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome = linha.strip()
                if nome:
                    lista_nomes.append(nome)
        print('Conteúdo do arquivo lido com sucesso:')
    except FileNotFoundError:
        print('Arquivo não encontrado. Uma nova lista será iniciada.')
if __name__ == '__main__':
    ler_arquivo()

while opcoes != 6:
    print('=' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('=' * 40)
    sleep(0.5)

    print(' CADASTROS DE NOMES '.center(40, '-'))
    print('1 - Adicionar\n' \
    '2 - Mostrar\n' \
    '3 - Remover\n' \
    '4 - Ordenar\n' \
    '5 - Salvar\n' \
    '6 - Sair')
    print('=-'*20)
    sleep(0.5)

    opcoes = int(input('Escolha uma das opções: '))
    print('=-'*20)
    sleep(0.5)

    if opcoes == 1:
        sleep(0.5)
        nomes = input('Adicione um nome: ')
        lista_nomes.append(nomes)
        print('NOME ADICIONADO COM SUCESSO.')
        print('=-'*20)
        sleep(0.5)

    elif opcoes == 2:
        print('Lista de nomes'.center(40))
        for n in lista_nomes:
            print(f"- {n}")
        print('=-'*20)
        sleep(0.5)


    elif opcoes == 3:
        remover = input('Qual nome você desja remover?: ')
        if remover in lista_nomes:
            lista_nomes.remove(remover)
            print('NOME REMOVIDO COM SUCESSO')
        else:
            print('Nome não encontrado na lista.')
        print('=-'*20)
        sleep(0.5)

    elif opcoes == 4:
        lista_nomes.sort()
        print('Lista em Ordem Alfabética'.center(40))
        print(lista_nomes)
        sleep(0.5)

    elif opcoes == 5:
        with open('listanomes.txt', 'w', encoding='utf-8') as arquivo:
            for nome in lista_nomes:
                arquivo.write(f"{nome}\n")
        print("DADOS SALVOS COM SUCESSO!")
        print('=-'*20)
        sleep(0.5)

    elif opcoes == 6:
        print('Programa finalizado.')
        print('=-'*20)
        sleep(0.5)

    else:
        print('Opção inválida, tente novamente.')
        print('=-'*20)
        sleep(0.5)
# Dia 12
# Salvar em arquivo TXT.
# Dia 13
# Ler os dados do TXT ao iniciar.
# Dia 14
# Refatoração.
# Melhore o código.
# Crie funções.

from time import sleep
lista_nomes = []
opcoes = 0
save_nomes = lista_nomes

# ------------------------------FUNÇÕES------------------------------

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

def adicionar():
    sleep(0.5)
    nomes = input('Adicione um nome: ')
    lista_nomes.append(nomes)
    print('NOME ADICIONADO COM SUCESSO.')
    print('=-'*20)
    sleep(0.5)

def mostrar():
    print('Lista de nomes'.center(40))
    for n in lista_nomes:
        print(f"- {n}")
    print('=-'*20)
    sleep(0.5)

def remover():
    remover = input('Qual nome você desja remover?: ')
    if remover in lista_nomes:
        lista_nomes.remove(remover)
        print('NOME REMOVIDO COM SUCESSO')
    else:
        print('Nome não encontrado na lista.')
    print('=-'*20)
    sleep(0.5)

def ordenar():
    lista_nomes.sort()
    print('Lista em Ordem Alfabética'.center(40))
    print(lista_nomes)
    sleep(0.5)

def salvar():
    with open('listanomes.txt', 'w', encoding='utf-8') as arquivo:
        for nome in lista_nomes:
            arquivo.write(f"{nome}\n")
    print("DADOS SALVOS COM SUCESSO!")
    print('=-'*20)
    sleep(0.5)

def sair():
    print('Programa finalizado.')
    print('=-'*20)
    sleep(0.5)

def opcao_invalida():
    print('Opção inválida, tente novamente.')
    print('=-'*20)
    sleep(0.5)

# ---------------------------CÓDIGO----------------------------------

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
        adicionar()

    elif opcoes == 2:
        mostrar()

    elif opcoes == 3:
        remover()

    elif opcoes == 4:
        ordenar()

    elif opcoes == 5:
        salvar()

    elif opcoes == 6:
        sair()

    else:
        opcao_invalida()
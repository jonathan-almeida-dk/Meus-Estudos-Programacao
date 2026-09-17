from pathlib import Path

lista_nomes = []

CAMINHO_ARQUIVO = Path(__file__).parent / 'lista.txt'


def ler_arquivo():
    lista_nomes.clear()

    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome = linha.strip()

                if nome:
                    lista_nomes.append(nome)

        print('Conteúdo do arquivo lido com sucesso.')

    except FileNotFoundError:
        print('Arquivo não encontrado. Uma nova lista será iniciada em MenuPrincipal.')


def cadastrar_pessoas():
    print('-' * 40)

    nome = input('Adicione uma pessoa: ').strip()

    if nome:
        with open(CAMINHO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}\n')

        print('NOME ADICIONADO COM SUCESSO.')

    else:
        print('ERRO: o nome não pode ficar vazio.')

    print('-' * 40)


def cadastrados():
    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)

    ler_arquivo()

    if not lista_nomes:
        print('Nenhuma pessoa cadastrada.')
    else:
        for nome in lista_nomes:
            print(f'- {nome}')

    print('-' * 40)
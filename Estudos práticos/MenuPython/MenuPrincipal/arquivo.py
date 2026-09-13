lista_nomes = []

def ler_arquivo():
    try:
        with open('lista.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome = linha.strip()
                if nome:
                    lista_nomes.append(nome)
        print('Conteúdo do arquivo lido com sucesso:')
    except FileNotFoundError:
        print('Arquivo não encontrado. Uma nova lista será iniciada.')

def cadastar_pessoas():
    print('-'*40)
    nome = input('Adicione uma pessoa: ')
    lista_nomes.append(nome)
    with open('lista.txt', 'w', encoding='utf-8') as arquivo:
        for nome in lista_nomes:
            arquivo.write(f'{nome}\n')
    print('NOME ADICIONADO COM SUCESSO.')
    print('-'*40)

def cadastrados():
    print('-'*40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-'*40)
    for n in lista_nomes:
        print(f'- {n}')
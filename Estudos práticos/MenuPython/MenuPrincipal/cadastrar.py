from arquivo import lista_nomes
def cadastar_pessoas():
    nome = input('Adicione uma pessoa: ')
    lista_nomes.append(nome)
    print('NOME ADICIONADO COM SUCESSO.')
    print('-'*40)
    
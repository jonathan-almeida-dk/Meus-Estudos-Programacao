import arquivo

def menu_principal():
    if __name__ == '__main__':
        arquivo.ler_arquivo()
    while True:
        print('-'*40)
        print('MENU PRINCIPAL'.center(40))
        print('-'*40)
        print('1 - Ver pessoas cadastradas' \
        '\n2 - Cadastrar nova pessoa' \
        '\n3 - Sair do Sistema')
        resp = int(input('Sua opção: '))
        if resp == 1:
            arquivo.cadastrados()
            continue
        elif resp == 2:
            arquivo.cadastar_pessoas()
            continue
        elif resp == 3:
            break
menu_principal()
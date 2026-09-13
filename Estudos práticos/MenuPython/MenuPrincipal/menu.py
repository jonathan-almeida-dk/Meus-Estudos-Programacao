
from MenuPrincipal import arquivo
from time import sleep as sl

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
        try:
            resp = int(input('Sua opção: '))
            if resp == 1:
                arquivo.cadastrados()
                sl(1.5)
                continue
            elif resp == 2:
                arquivo.cadastar_pessoas()
                sl(1.5)
                continue
            elif resp == 3:
                print('ENCERRANDO SISTEMA...')
                sl(1.5)
                break
            else:
                print('ERRO: por favor, digite um NÚMERO válido.')
                sl(1)
                continue
        except (KeyboardInterrupt):
            print('\nUsuário preferiu não digitar um NÚMERO.')
            sl(1)
            return 3
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um NÚMERO inteiro válido.')
            sl(1)
            continue
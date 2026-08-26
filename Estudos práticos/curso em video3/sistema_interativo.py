# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.



def sistema():
# ================================================================
    # TELA INICIAL
    def inicio():
        print('\033[30;42m')
        print('~'*42)
        print('SISTEMA DE AJUDA PyHelp'.center(42))
        print('~'*42, end='')
        print('\033[m')

# ================================================================
    # TELA DE ACESSO
    def acesso():
        print('\033[30;44m')
        print('~'*42)
        print(f'Acessando o manual do comando {param}'.center(42))
        print('~'*42, end='')
        print('\033[m')

# ================================================================
    while True:
        inicio()
        param = input('Função ou Biblioteca > ')
        acesso()
        help(param)

        if param in 'FIMfim':
            print('\033[30;41m')
            print('~'*20)
            print(f'Até logo!'.center(20))
            print('~'*20, end='')
            print('\033[m')
            break

sistema()
        
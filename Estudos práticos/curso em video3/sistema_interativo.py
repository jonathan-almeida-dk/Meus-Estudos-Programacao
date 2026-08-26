# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep
c= ('\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m'        # 6 - branco
    )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'* tam)
    print(f'   {msg}')
    print('~'* tam)
    print(c[0], end='')
    sleep(1)

# PROGRAMA PRINCIPAL
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = (input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
















# PRIMEIRA SOLUÇÃO

# def sistema():
# # ================================================================
#     # TELA INICIAL
#     def inicio():
#         print('\033[30;42m')
#         print('~'*42)
#         print('SISTEMA DE AJUDA PyHelp'.center(42))
#         print('~'*42, end='')
#         print('\033[m')

# # ================================================================
#     # TELA DE ACESSO
#     def acesso():
#         print('\033[30;44m')
#         print('~'*42)
#         print(f'Acessando o manual do comando {param}'.center(42))
#         print('~'*42, end='')
#         print('\033[m')

# # ================================================================
#     while True:
#         inicio()
#         param = input('Função ou Biblioteca > ')
#         acesso()
#         help(param)

#         if param in 'FIMfim':
#             print('\033[30;41m')
#             print('~'*20)
#             print(f'Até logo!'.center(20))
#             print('~'*20, end='')
#             print('\033[m')
#             break

# sistema()
        


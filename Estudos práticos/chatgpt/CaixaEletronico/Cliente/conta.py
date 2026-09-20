from time import sleep as sl

nome = input(f'Nome: ')
saldoInicial = float(input(f'Saldo Inicial da Conta: R$'))
sl(1)

def cabeçalho(titulo=''):

    print('='*40)
    print(titulo.center(40))
    print('='*40)


def consulta():
        cabeçalho('CAIXA ELETRÔNICO')
        print(f'Nome: {nome}')
        print(f'Saldo atual: R${saldoInicial:.2f}')
        sl(1)


def depositar():

    while True:

        global saldoInicial

        try:
            dep = float(input('Quanto deseja depositar? R$'))

            if dep > 0:
                
                saldoInicial += dep
                
                print('Depositando valor...')
                sl(1.2)
                print(f'Deposito de R${dep:.2f} efetuado com sucesso!')
                print(f'Na sua conta consta R${saldoInicial:.2f}.')
                sl(1.2)
                return saldoInicial
            else:
                print('ERRO: número abaixo do permitido! Tente novamente.')
                print('='*40)
                sl(1.2)
                continue

        except ValueError:
            print('ERRO: digite apenas valores numéricos!')
            print('='*40)
            sl(1.2)


def sacar():

    global saldoInicial

    while True: 


        try:
            saque = float(input('Digite o valor de saque: '))
            print('Processando...')
            sl(0.5)

            if 0 < saque <= saldoInicial:

                print('Realizando saque...')
                sl(1.2)
                saldoInicial -= saque
                print(f'Saque de R${saque:.2f} efetuado com sucesso!')
                print(f'Na sua conta consta R${saldoInicial:.2f}.')

            else:
                print('Valor inválido, tente novamente.')
                print('='*40)
                sl(1)
                continue


            return saldoInicial
        except ValueError:
                    print('ERRO: digite apenas valores numéricos!')
                    print('='*40)
                    sl(1)



def  menu():
    while True:

        try:
             
            cabeçalho('CAIXA ELETRÔNICO')

            resp = int(input('1 - Consultar saldo: \n' \
            '2 - Depositar: \n' \
            '3 - Sacar: \n' \
            '4 - Sair: \n' \
            'Resposta: '))
            sl(1)

            print('='*40)

            # ===== CONDIÇÕES ======
            if resp == 1:
                consulta()
            elif resp == 2:
                depositar()
            elif resp == 3:
                if saldoInicial == 0:
                    print('Sua conta não possui valores a serem sacados!')
                    continue
                sacar()
            elif resp == 4:
                print('ENCERRANDO SISTEMA...')
                sl(1.2)
                print('SISTEMA ENCERRADO')
                break
            else:
                 print('Opção inválida! Digite uma opção entre 1 e 4.')
                 sl(1)
                 continue
            
            return resp
        except ValueError:
            print('ERRO: digite apenas valores numéricos!')
            print('='*40)
            sl(1)
menu()

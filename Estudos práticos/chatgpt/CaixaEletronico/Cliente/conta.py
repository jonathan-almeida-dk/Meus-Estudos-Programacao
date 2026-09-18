
nome = input(f'Nome: ')
saldoInicial = int(input(f'Saldo Inicial da Conta: '))

def cabeçalho(titulo=''):

    print('='*40)
    print(titulo.center(40))
    print('='*40)
cabeçalho('CAIXA ELETRÔNICO')


def  menu():

    resp = int(input('1 - Consultar saldo: \n' \
    '2 - Depositar: \n' \
    '3 - Sacar: \n' \
    '4 - Sair: '))
    print('='*40)
    return resp

def consulta():

        cabeçalho('CONSULTA')
        print(f'Nome: {nome}')
        print(f'Saldo atual: {saldoInicial}')


def depositar():
    while True:

        try:
            dep = float(input('Quanto deseja depositar? '))

            if dep >= 0:
                saldoInicial += dep
                return saldoInicial
            else:
                print('ERRO: número abaixo do permitido! Tente novamente.')
                continue
        except ValueError:
            print('ERRO: digite apenas valores numéricos!')


def sacar():
    saque = float(input('Digite o valor de saque: '))
    if saque > 0:
        saldoInicial -= saque
        return saldoInicial
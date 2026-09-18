
nome = input(f'Nome: ')
saldo = int(input(f'Saldo Inicial da Conta: '))

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
        nome = input(f'Nome: {nome}')
        saldo = int(input(f'Saldo: {saldo}'))
        print(f'Nome: {nome}')
        print(f'Saldo: {saldo}')

# def depositar():





# def sacar():




# def sair():


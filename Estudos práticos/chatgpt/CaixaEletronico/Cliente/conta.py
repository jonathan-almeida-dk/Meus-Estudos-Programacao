import sys
import os

# Linha mágica temporária para o Python achar o 'sistema.py' lá atrás
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Seus imports de teste
from sistema import nome, saldo

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
        print(f'Saldo: {saldo}')
    

# def depositar():




# def sacar():




# def sair():


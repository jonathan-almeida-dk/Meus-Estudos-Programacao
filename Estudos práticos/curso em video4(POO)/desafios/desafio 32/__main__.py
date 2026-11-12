from conta import *

def main():
    cc = ContaBancaria(111, 'Jonas', 15000, 'olamundo')

    print('Vou tentar sacar...')
    cc.sacar(500)

    print('Tentando mudar o nome...')
    cc.nome = 'Maria'

    print(cc)

if __name__ == '__main__':
    main()
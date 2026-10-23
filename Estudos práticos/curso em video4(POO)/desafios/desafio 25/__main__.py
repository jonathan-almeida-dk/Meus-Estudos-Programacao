from rich import print
from transporte import *
from rich.table import Table

def main():
    dist = 80

    '''
    entrega = Drone(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.cal_frete()}.')
    '''
    
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title='Tabela de Fretes')
    tabela.add_column('Distancia')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')

    for item in viagem:
        tabela.add_row(f'{dist}Km',f'{type(item).__name__}',f'{item.cal_frete()}')

    print(tabela)


if __name__ == '__main__':
    main()

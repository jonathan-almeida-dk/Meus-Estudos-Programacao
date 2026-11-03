from rich import inspect
from diario import *

def main():
    d = Diario()
    d.escrever('Olá, mundo')
    d.escrever('Programando!')
    try:
        d.ler('123456')
    except Exception as e:
        print(f'[red]ERRO: {e}')

    # inspect(d,private=True)







if __name__ == '__main__':
    main()
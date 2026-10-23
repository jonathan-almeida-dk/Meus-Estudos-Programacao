from rich import print, inspect
from cafeteria import *

def main():
    cha = Cha()
    inspect(cha, methods= True)
    print(f'Seu {} está pronto.')
    cafe = Cafe()
    inspect(cafe, methods= True)
    print(f'Seu {} está pronto.')

    leite = Leite()
    inspect(leite, methods= True)
    print(f'Seu {} está pronto.')

if __name__ == '__main__':
    main()
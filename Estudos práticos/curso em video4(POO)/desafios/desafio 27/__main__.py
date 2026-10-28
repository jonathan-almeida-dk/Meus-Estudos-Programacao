from rich import inspect
from personagem_rpg import *

def main():
    p1 = Guerreiro('Kratos', 1000)
    p2 = Mago('Merlin', 1500)

    print()
    p1.atacar(p2, 100)
    print()
    p2.curar()
    print()
    print()
    p2.atacar(p1)
    print()
    p1.curar()




    

if __name__ == '__main__':
    main()
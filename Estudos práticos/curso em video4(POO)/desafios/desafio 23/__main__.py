from rich import print, inspect
from poligono import *

def main():
    q = Quadrado(5)
    inspect(q, methods= True)
    print(f'Perímetro = {q.perimetro():.1f}mm')
    print(f'Area = {q.area():.1f}mm²')

    print()
    
    c = Circulo(5)
    inspect(c, methods= True)
    print(f'Perímetro = {c.perimetro():.1f}mm')
    print(f'Area = {c.area():.1f}mm²')

if __name__ == '__main__':
    main()
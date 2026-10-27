from rich import inspect
from funcionarios import *

def main():
    f1 = Horista('José', 12, 200)
    f1.calcular_salario()
    f1.analisar_salario()
    print()
    f2 = Mensalista('Paulo', 9500)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == '__main__':
    main()
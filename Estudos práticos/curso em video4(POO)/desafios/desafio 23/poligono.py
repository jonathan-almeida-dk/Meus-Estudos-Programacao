# Implemente o seguinte diagrama de classes:

# Poligono {abstract}     <--- Classe Mãe
#     + qtd_lados
#     + perimetro() {abstract}
#     + area() {abstract}


# Quadrado
#     + lado
#     + perimetro()
#     + area()

# Circulo
#     + raio
#     + perimetro()
#     + area()

from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self):
            self.perimetro = self.raio * 4
    
    def area(self):
        self.area = self.raio ** 2

class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    pass
# Crie uma classe Produto, onde podemos cadastrar nome e o preço.
# Crie também um método que mostre uma etiqueta de preço do produto.
from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto:

    def __init__(self, nome, preço): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        print(Panel(Align.center(f'{self.nome}\nR${self.preço}',),
                       title='Produto',
                       style='white',
                       width=40,
                       height=5,
                       ))


p1 = Produto('Iphone 17 Pro Max', preço=25_000.85)
p2 = Produto('Notebook Gamer', preço=8_000)

p1.etiqueta()
p2.etiqueta()
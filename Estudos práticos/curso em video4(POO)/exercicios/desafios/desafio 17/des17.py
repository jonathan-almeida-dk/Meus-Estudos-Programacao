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
        conteudo = f'{self.nome.center(30,' ')}'
        conteudo += f'{'-'*30}'
        preçof = f'R${self.preço:,.2f}'
        conteudo += f'{preçof.center(30, '.')}'
        etiqueta = Panel(conteudo,title='Produto', width=34)
        print(etiqueta)


p1 = Produto('Iphone 17 Pro Max', preço=25_000.85)
p1.etiqueta()

p2 = Produto('Notebook Gamer', preço=8_000)
p2.etiqueta()

# Crie uma classe 'Churrasco', onde seja possível informar 'quantas
#  pessoas' vão participar e mostre 'quanto de carne' deve ser comprado,
# o 'custo total' do churrasco e o 'preço por pessoa.'
from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant): # método construtor
        # atributos de instância
        self.title = titulo
        self.quant_pes = quant
        self.car = 0.400
        self.preço = 82.4

    # métodos de instância
    def analisar(self):
        peso_total_carne = self.car * self.quant_pes
        valor_carne_pessoa = (self.preço / 1000) * 400
        valor_total = self.quant_pes * valor_carne_pessoa
        tabela = Panel(f'Analisando [green]{self.title}[/] com [blue]{self.quant_pes} convidados[/]'
                       f'\nCada participante comerá {self.car:.2f}g e cada Kg custa R${self.preço:.2f}'
                       f'\nRecomendo comprar [yellow]{peso_total_carne:.3f}Kg[/] de carne'
                       f'\nO custo total será de [green]R${valor_total:.2f}[/]'
                       f'\nCada pessoa pagará [purple]R${valor_carne_pessoa:.2f}[/] para participar.',title=self.title)
        print(tabela)
        


# Declaração de objetos

c1 = Churrasco('Churras dos Amigos', 2)

c1.analisar()
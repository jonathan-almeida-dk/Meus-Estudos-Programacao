from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
# ==============================================================================
# ==============================================================================

class Funcionario(ABC):
    salario_minimo = 1612
    inss = 0.075
    def __init__(self,nome,salario_bruto,salario):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = salario

    def analisar_salario(self):
        pass

    @abstractmethod
    def calcular_salario(self):
        pass
# ==============================================================================
# ==============================================================================

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, qtd_horas):
        super().__init__(nome,0, 0)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_salario(self):
        self.salario_bruto = self.valor_hora * self.qtd_horas
        self.desconto = self.salario_bruto * self.inss
        self.valor_final = self.salario_bruto - self.desconto
        self.salario = self.valor_final / self.salario_minimo

        conteudo = f'O salário de [blue]{self.nome}[/] ([purple]{Horista.__name__}[/]) é de [green]R${self.valor_final}[/] e corresponde a [yellow]{self.salario:.1f} salários mínimos[/].'
        etiqueta = Panel(conteudo,title='Análise de Salário', width=60)
        print(etiqueta)
        
    
# ==============================================================================
# ==============================================================================

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome, salario_bruto, 0)

    def calcular_salario(self):
        self.desconto = self.salario_bruto * self.inss
        self.valor_final = self.salario_bruto - self.desconto
        self.salario = self.valor_final / self.salario_minimo

        conteudo = f'O salário de [blue]{self.nome}[/] ([purple]{Mensalista.__name__}[/]) é de [green]R${self.valor_final}[/] e corresponde a [yellow]{self.salario:.1f} salários mínimos[/].'
        etiqueta = Panel(conteudo,title='Análise de Salário', width=60)
        print(etiqueta)


# ==============================================================================
# ==============================================================================


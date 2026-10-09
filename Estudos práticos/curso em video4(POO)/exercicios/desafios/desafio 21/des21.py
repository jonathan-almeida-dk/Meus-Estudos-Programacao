# Crie a classe Caneta, que simule o funcionamento de  uma 
# caneta colorida, podendo escrever frases na cor relativa
from rich import print

class caneta:
    def __init__(self, cor = 'azul'): # Método Construtor
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'
        
        self.cor = escolha
        self.tampada = True


    # Métodos de Instância
    def escrever(self,msg):
        if self.tampada:
            print(f':prohibited: A {self.cor} caneta[/] está tampada!')
        else:
            print(f'{self.cor}{msg}[/]', end='')

    
    def quebrar_linha(self,qtd = 1):
        print('\n' * qtd, end='')


    def tampar(self):
        self.tampada = True
        
    def destampar(self):
        self.tampada = False

# Declaração de Objetos

c1 = caneta('azul')
c2 = caneta('vermelha')
c3 = caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, Mundo!')
c1.quebrar_linha(3)

c2.escrever('Funciona!')
c2.quebrar_linha(5)

c3.escrever('Deu certo!')
c3.quebrar_linha(10)

c1.tampar()
c1.escrever('Será que rola?')
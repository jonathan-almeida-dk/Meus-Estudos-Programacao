from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):
    def __init__(self,nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 50):
        if self.vida > 0 and alvo.vida > 0:
            # vai atacar
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'[blue]{self.nome}[/]({self.vida}) atacou [green]{alvo.nome}[/]({alvo.vida}) com um [red]{golpe}[/] de força [yellow]{forca}[/]')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer.')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu dano de [red]{fator}[/]!')
        print(f'{self.nome} = Vida({self.vida})')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Machado', 'Chute']


    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] enrolou atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida.')
        print(f'{self.nome} = Vida({self.vida})')


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Bola de Gelo', 'Explosão de Raios']


    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] fez magia de cura e [green]recuperou {fator} pontos[/] de vida.')
        print(f'{self.nome} = Vida({self.vida})')
    
        
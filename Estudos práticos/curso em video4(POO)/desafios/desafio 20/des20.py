# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie também um método que permita mostrar a ficha desse gamer.
from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:
    def __init__(self, nome, nick): # método construtor
        # atributos de instância
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    # métodos de instância

    def add_favoritos(self,game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Nome real: [black on blue] {self.nome} [/]'
        conteudo += f'\nJogos favoritos:'

        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue]{game}[/]'
        painel = Panel(conteudo,title=f'Jogador <{self.nick}>', width=40)
        print(painel)

j1 = Gamer('Jonathan', 'Darkspace')
j1.add_favoritos('God of War')
j1.add_favoritos('God of War2')
j1.add_favoritos('Fortnite')
j1.add_favoritos('Red Dead Redemption')
j1.add_favoritos('GTA V')
# inspect(j1)
j1.ficha()

j2 = Gamer('Pedro', 'detonator')
j2.add_favoritos('Mario Bros')
j2.add_favoritos('Sonic')
j2.add_favoritos('PUBG')
j2.add_favoritos('Forza')
j2.add_favoritos('Mortal Kombat')
# inspect(j2)
j2.ficha()
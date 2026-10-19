# Crie a classe Livro, que vai simular a passagem de páginas
# de um livro, considerando também se usuário chegou ao fim da leitura.
from rich import print
from time import sleep

class livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(
            f'📖 Você acabou de abrir o livro "[green]{self.titulo}[/]"\n'
             f' que tem [red]{self.total_paginas} páginas[/] no total.Você está na [yellow]{self.pagina_atual}[/].'
            )
    
    def avancar_paginas(self,qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f' Pág{self.pagina_atual} ▶️', end=' ')
                sleep(0.3)
                cont += 1
        print(f'\nVocê avançou {cont} páginas e está na [blue]página {self.pagina_atual}[/]')
        if self.fim_do_livro():
            print(f'📕 [red]Você chegou ao final do livro "{self.titulo}"[/]')

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False


l1 = livro('10 coisas que aprendi', 10)
l1.avancar_paginas(3)
l1.avancar_paginas(4)
l1.avancar_paginas(3)
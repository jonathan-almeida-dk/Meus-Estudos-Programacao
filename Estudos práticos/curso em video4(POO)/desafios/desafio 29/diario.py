from rich import print
from rich.panel import Panel
class Diario():
    def __init__(self):
        self.__segredos = []
        self.__senha = 123456

    def escrever(self,msg):
        self.__segredos.append(msg)
        return self.__segredos

    def ler(self, senha):
        try:
            if  senha != self.__senha:
                raise PermissionError
            print('[green]Diário Liberado[/]')
            for indice, segredo in  enumerate(self.__segredos,start=1):
                print(Panel(
                    f'[italic]{segredo}[/]',
                    title=f'Página {indice}',
                    border_style= 'cyan',
                    expand=False
                ))
        except PermissionError:
            print('Você não pode ler o diário!')
            


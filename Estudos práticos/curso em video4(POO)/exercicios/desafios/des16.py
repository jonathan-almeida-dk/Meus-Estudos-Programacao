# Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.
from rich import print

class funcionario:
    def __init__(self): # Método Construtor

        # Atributos de Instância
        self.nome = 'José'
        self.setor = 'Administrativo'
        self.cargo = 'Gerente'

    # Métodos de Instância
    def apresentacao(self):
        return f'Sou {self.nome} do setor {self.setor} e meu cargo é {self.cargo}. :handshake:'

    
# Declaração dos objetos

fun = funcionario()
print(fun.apresentacao())


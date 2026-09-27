# Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.
from rich import print

class funcionario:
    def __init__(self,nome, Setor, Cargo): # Método Construtor

        # Atributos de Instância
        self.nome = nome
        self.setor = Setor
        self.cargo = Cargo

    # Métodos de Instância
    def apresentacao(self):
        return f'Sou {self.nome} do setor {self.setor} e meu cargo é {self.cargo}. :handshake:'

    
# Declaração dos objetos

c1 = funcionario('José','Administrativo','Gerente')
print(c1.apresentacao())

c2 = funcionario('Luan','TI','Programador')
print(c2.apresentacao())



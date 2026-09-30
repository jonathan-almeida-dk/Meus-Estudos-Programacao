# Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.
from rich import print
from rich import inspect

class funcionario:
    # Atributos de classe
    empresa = 'Curso em vídeo'

    def __init__(self,nome, Setor, Cargo): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.setor = Setor
        self.cargo = Cargo

    # Métodos de Instância
    def apresentacao(self):
        return f'Sou [blue]{self.nome}[/] do setor {self.setor} e meu cargo é {self.cargo} na empresa {funcionario.empresa}. :handshake:'
        # NOTAS:
        # Também é possível usar prints nas funções, porém, é necessário retirar o print no final    >>>    print(c1.apresentacao())    >>>>     c1.apresentacao()
        # print(f'Sou [blue]{self.nome}[/] do setor {self.setor} e meu cargo é {self.cargo}. :handshake:')

    
# Declaração dos objetos

# funcionario.empresa = 'Hostnet' # Fazendo isso a 'empresa' muda para todos os funcionários, PERIGOSO!

c1 = funcionario('José','Administrativo','Gerente')
print(c1.apresentacao())
inspect(c1)

c2 = funcionario('Luan','TI','Programador')
print(c2.apresentacao())
inspect(c2)

inspect(funcionario)

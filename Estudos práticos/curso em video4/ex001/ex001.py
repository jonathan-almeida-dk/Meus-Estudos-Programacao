# Declaração da classe

class Gafanhoto:
    def __init__(self): # Método Construtor

        # Atributos de Instância
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


# Declaração dos objetos

g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())
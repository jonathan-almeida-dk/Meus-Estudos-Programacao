# Declaração da classe

class Gafanhoto:
    def __init__(self): # Método Construtor

        # Atributos de Instância
        self.nome = ''
        self.idade = 0
        self.sexo = ''

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a), tem {self.idade} anos de idade e seu sexo é {self.sexo}.'
    
    def Sexo(self):
        self.sexo = input('Qual o sexo dele(a)?: ')


# Declaração dos objetos

print('-'*30)
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
g1.Sexo()
print(g1.mensagem())

print('-'*30)
g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario()
g2.Sexo()
print(g2.mensagem())

print('-'*30)
g3 = Gafanhoto()
g3.nome = input('Qual o seu nome?: ')
g3.idade = input('Qual a sua idade?: ')
g3.Sexo()
print(g3.mensagem())
print('-'*30)
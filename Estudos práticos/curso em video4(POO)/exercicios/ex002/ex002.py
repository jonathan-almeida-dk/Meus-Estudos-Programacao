# Declaração da classe

class Gafanhoto:
    '''
    Essa classe cria um Gafanhoto, que é uma pesoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    '''
    def __init__(self, nome = 'vazio', idade = 0): # Método Construtor

        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a), tem {self.idade} anos de idade..'
    
    def __get__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# ====================================================================

# Declaração dos objetos

print('='*60)

g1 = Gafanhoto('Maria', 17)
g1.aniversario()
print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method

# ====================================================================

print('='*60)

print(g1.__doc__) # Dunder Attribute DOCSTRING

print('='*60)

# ====================================================================

g2 = Gafanhoto('Mauro', 54)
print(g2)
print(g2.__getstate__())

print('='*60)

# ====================================================================
from rich import print

class Solicitacao:
    def __init__(self, titulo, descricao, solicitante = 'Vazio'): # Método Construtor
        # Atributos de Instância
        self.titulo = titulo
        self.descricao = descricao
        self.solicitante = solicitante

    # Métodos de Instância
    def descrita(self):
        conteudo = f'Olá, essa é uma solicitacao de {self.solicitante}!'
        return conteudo


# Declaração de Objetos

sol = Solicitacao('Solicitação', 'Nâo consigo acessar os sistema.', 'Ana' )
print(sol.descrita())
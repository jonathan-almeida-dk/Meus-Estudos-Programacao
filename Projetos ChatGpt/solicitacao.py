
class Solicitacao:
    def __init__(self, titulo, descricao, solicitante='Vazio',prioridade='media', status='aberta'):
        self.titulo = titulo
        self.descricao = descricao
        self.solicitante = solicitante
        self.prioridade = prioridade
        self.status = status

    def descrita(self):
        conteudo = f'Olá, essa é uma solicitação de {self.solicitante}!'
        conteudo += f'\nPrioridade: {self.prioridade}'
        conteudo += f'\nStatus: {self.status}'
        return conteudo

    def atualizar_status(self,novo_status):
        status_permitidos = ('aberta', 'concluída', 'em andamento')
        if novo_status in status_permitidos:
            self.status = novo_status
            print('Status atualizado com sucesso!')
        else:
            print('Status inválido! Escolha: aberta, em andamento ou concluída.')


sol = Solicitacao(
    'Erro: Sistema',
    'Não consigo acessar o sistema.',
    'Ana'
    )

sol2 = Solicitacao(
    'Acesso ao e-mail',
    'Não consigo acessar minha conta.',
    'José',
    'Alta'
    )

print('-='*40)
sol.atualizar_status('resolvida')
print(sol.descrita())
print('-='*40)

sol2.atualizar_status('em andamento')
print(sol2.descrita())
print('-='*40)
from rich import print

class Solicitacao:
    def __init__(self, titulo, descricao, solicitante='[black on white] vazio [/]',prioridade='[yellow]media[/]', status='[green]aberta[/]'):
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
            resultado = True
            return resultado
        else:
            resultado = False
            return resultado




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

sol3 = Solicitacao(
    'Envio de Formulário',
    'Erro de envio de formulário',
)


# =====================================================================

# Solicitação1

print('-='*40)
resultado = sol.atualizar_status("resolvida")
if resultado:
    print("[green]Status atualizado![/]")
else:
    print("[red]Status inválido![/]")
print()

print(f'Resultado: {resultado}')
print(sol.descrita())
print('-='*40)

# =====================================================================

# Solicitação2

resultado = sol2.atualizar_status("em andamento")
if resultado:
    print("[green]Status atualizado![/]")
else:
    print("[red]Status inválido![/]")
print()

print(f'Resultado: {resultado}')
print(sol2.descrita())
print('-='*40)

# =====================================================================

# Solicitação3

resultado = sol3.atualizar_status("em andamento")
if resultado:
    print("[green]Status atualizado![/]")
else:
    print("[red]Status inválido![/]")
print()

print(f'Resultado: {resultado}')
print(sol3.descrita())
print('[green] [ LAÇO FOR ] [/]'.center(80, '='))

# =====================================================================
solicitacoes = [sol, sol2, sol3]

for solicitacao in solicitacoes:
    print(solicitacao.descrita())
    print("-" * 40)
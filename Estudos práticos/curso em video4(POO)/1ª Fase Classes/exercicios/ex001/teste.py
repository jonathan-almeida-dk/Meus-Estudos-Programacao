from rich import print
from rich.align import Align
from rich.panel import Panel

# 1. Crie o conteúdo envolvido na função Align.center
conteudo_centralizado = Align.center("Texto centralizado!")

# 2. Passe para o Panel (use title_align="center" se quiser o título no meio)
meu_painel = Panel(
    conteudo_centralizado,
    title="Título Centralizado",
    title_align="center",
    width=40,
    height=5
)

print(meu_painel)

from rich import print, inspect
from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

# ====================================================================================

a1 = Aluno('Jonathan', 26, 'Informática', 'T01')
a1.fazer_aniversario()
inspect(a1, methods=True)
a1.fazer_matricula()

# ====================================================================================

p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
p1.fazer_aniversario()
inspect(p1, methods=True)
p1.dar_aula()

# ====================================================================================

f1 = Funcionario('José', 54, 'Atendente', 'Técnico')
f1.fazer_aniversario()
inspect(f1, methods=True)
f1.bater_ponto()
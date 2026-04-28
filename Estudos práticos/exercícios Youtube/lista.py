notas = []

for x in range(10):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantodade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota= n[1]
    print("0 RM", codigo_aluno, "tirou a nota:", nota)
    
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

cursor.execute("""
INSERT INTO alunos (nome, idade)
VALUES (?, ?)
""", (nome, idade))

conexao.commit()

print("Aluno cadastrado!")
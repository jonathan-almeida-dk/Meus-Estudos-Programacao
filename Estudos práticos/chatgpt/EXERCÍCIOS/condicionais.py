import os
os.system("cls")

#Perguntas
nome = input("Qual é o seu nome?: ")
idade = int(input("Quantos anos você tem? "))

os.system("cls")

#Resultado Final
print("Seu nome é", nome,".")
if idade > 18:
    print("Você já pode tirar sua habilitação.")
elif idade == 18:
    print("Você acabou de atingir a idade para tirar a habilitação!")
else:
    print("Ainda não pode tirar a habilitação.")

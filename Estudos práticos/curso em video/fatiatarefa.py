import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

clear

frase = 'Curso em Video Python'
print(len(frase))
print(frase.upper())
print(frase.lower())
junçao = ''.join(frase.split())
print(len(junçao))

divisao = frase.split()
print(len(divisao[0]))

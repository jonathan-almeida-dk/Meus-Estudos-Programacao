import os
os.system("cls" if os.name == "nt" else "clear")

print(" Verificador de números PARES ou ÍMPARES ".center(80,"="))
while True:
    try:
        n1 = int(input("Digite um número: "))

        if n1 % 2 ==0:
            print("Este número é PAR!")
        else:
            print("Este número é ÍMPAR")
        
        opcao = str(input("Deseja continuar? (s/n) ")).lower()

        if opcao == "n":
            print("Programa Encerrado.")
            break
        
    except ValueError:
        print("Entrada inválida!Digite apenas números.")



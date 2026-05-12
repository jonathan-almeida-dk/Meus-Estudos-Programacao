while True:
    try:
        numero = int(input("Digite um número: "))

        if numero % 2 ==0:
            print("O número é PAR")
        else:
            print("O número é ÍMPAR")
        
        continuar = input("Deseja testar outro número? (sim/não): ").strip().lower()

        if continuar == "não":
            print("Encerrando o programa. Até logo!")
            break #Sai do while
    except ValueError:
        print("Entrada inválida!Digite apenas números.")
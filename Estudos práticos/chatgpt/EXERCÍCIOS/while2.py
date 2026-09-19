# Contadores de pares e ímpares
total_pares = 0
total_impares = 0

while True:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número é PAR")
        total_pares += 1
    
    else:
        print("O número é ÍMPAR.")
        total_impares += 1
    
    continuar = input("Deseja testar outro número? (sim/não): ").strip().lower()
    
    if continuar == "não":
        print("\nEncerrando o programa...")
        break  # Sai do loop

# Resumo Final
print("\n---RESUMO---")
print(f"Total de números pares: {total_pares}")
print(f"Total de números ímpares: {total_impares}")
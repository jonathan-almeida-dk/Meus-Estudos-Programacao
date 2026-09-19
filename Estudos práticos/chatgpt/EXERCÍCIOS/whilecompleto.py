import os

total_pares = 0
total_impares = 0
soma_total = 0
quantidade_total = 0

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    limpar_tela()
    print("==== MENU ====")
    print("1 - Digitar um número")
    print("2 - Sair e ver o resumo")
    opcao = input("Escolha uma opção (1 ou 2): ").strip()

    if opcao == "2":
        break

    elif opcao == "1":
        try:
            entrada = float(input("Digite um número: ").strip())

        except ValueError:
            print("❌ Entrada inválida! Por favor, digite apenas números.")
            input("Pressione Enter para continuar...")
            continue  # Volta para o início do while

        soma_total += entrada
        quantidade_total += 1

        if entrada % 2 == 0:
            print("✅ O número é PAR.")
            total_pares += 1
        else:
            print("✅ O número é ÍMPAR.")
            total_impares += 1

        input("Pressione Enter para continuar...")

    else:
        print("❌ Opção inválida. Escolha 1 ou 2.")
        input("Pressione Enter para continuar...")

# Resumo final
limpar_tela()
print("===== RESUMO FINAL =====")
print(f"Total de números digitados: {quantidade_total}")
print(f"Total de números pares: {total_pares}")
print(f"Total de números ímpares: {total_impares}")

if quantidade_total > 0:
    media = soma_total / quantidade_total
    print(f"Média dos números digitados: {media:.2f}")
else:
    print("Nenhum número foi digitado.")

print("\nPrograma finalizado. Até a próxima! 👋")

import matplotlib.pyplot as plt

# Gráfico de Pizza: Pares vs Ímpares
labels = ['Pares', 'Ímpares']
valores = [total_pares, total_impares]
cores = ['skyblue', 'lightcoral']

plt.figure(figsize=(5,5))
plt.pie(valores, labels=labels, colors=cores, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Pares e Ímpares')
plt.axis('equal')
plt.show()

# Gráfico de Barras: Totais
plt.figure(figsize=(6,4))

plt.bar('Total', quantidade_total, color ='gray')
plt.bar('Pares', total_pares, color ='skyblue')
plt.bar('Ímpares', total_impares, color ='lightcoral')
if quantidade_total > 0:
    plt.bar('Média', soma_total / quantidade_total, color ='green')

plt.title('Resumo dos Números Digitados')
plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()



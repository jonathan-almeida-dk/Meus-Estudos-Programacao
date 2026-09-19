# =============================
# 📦 IMPORTAÇÃO DE BIBLIOTECAS
# =============================
import os
import time
import random
import matplotlib.pyplot as plt  # Remova se não for usar gráficos

# ======================
# ⚙️ VARIÁVEIS GLOBAIS
# ======================
dados = []  # Exemplo: lista para armazenar dados
rodando = True

# ======================
# 📌 FUNÇÕES PRINCIPAIS
# ======================

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("=== MENU ===")
    print("1 - Inserir número")
    print("2 - Ver gráfico")
    print("3 - Sair")

def inserir_numero():
    try:
        numero = int(input("Digite um número: "))
        dados.append(numero)
        print("Número salvo com sucesso!")
    except ValueError:
        print("❌ Valor inválido! Digite apenas números.")

def mostrar_grafico():
    if not dados:
        print("Nenhum dado para exibir.")
        return

    plt.figure()
    plt.plot(dados, marker='o')
    plt.title("Gráfico dos Números Digitados")
    plt.xlabel("Posição")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.show()

# ============================
# 🚀 PROGRAMA PRINCIPAL
# ============================
if __name__ == "__main__":
    while rodando:
        limpar_tela()
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            inserir_numero()
        elif opcao == "2":
            mostrar_grafico()
        elif opcao == "3":
            print("Encerrando o programa... Até logo!")
            rodando = False
        else:
            print("❌ Opção inválida!")

        input("\nPressione Enter para continuar...")

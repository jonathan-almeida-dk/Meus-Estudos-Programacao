import os
from time import sleep

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

print(f'\n{'MENU':=^41}')

print(f'\n{'➕ ➖ ➗ 🟰  ✖️':^40}')
print(f'{'CALCULADORA PROFISSIONAL':^43}')
print(f'{'➕ ➖ ➗ 🟰  ✖️':^40}')

# Funções das operações
def soma():
    resultado = n1 + n2
    print(f'SOMA: {n1:.1f} + {n2:.1f} = {resultado:.2f}')
    sleep(2.5)

def subtracao():
    resultado = n1 - n2
    print(f'SUBTRAÇÃO: {n1:.1f} - {n2:.1f} = {resultado:.2f}')
    sleep(2.5)

def multiplicacao():
    resultado = n1 * n2
    print(f'MULTIPLICAÇÃO: {n1:.1f} × {n2:.1f} = {resultado:.2f}')
    sleep(2.5)

def divisao():
    if n2 == 0:
        print('❌ Não é possível dividir por zero!')
        sleep(2.5)
        return
    resultado = n1 / n2
    print(f'DIVISÃO: {n1:.1f} ÷ {n2:.1f} = {resultado:.2f}')
    sleep(2.5)
while True:
    print('')
    print(f'{'MENU':=^41}')
    print('\nEscolha uma das opções aritméticas abaixo:')
    print('''\n    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Cancelar
        ''')
    try:
        opcao = int(input('Digite o número da opção: '))
    except ValueError:
        print('❌ Entrada inválida! Digite apenas números.')
        continue

    if opcao == 5:
        print(F'{'❌ AÇÃO CANCELADA ❌':^23}')
        break

    if opcao not in [1,2,3,4]:
        print('❌ Opção inválida! Escolha entre 1 e 5.')
        sleep(4)
        continue
    try:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print('🔄️ LOADING 🔄️')
    except ValueError:
        sleep(3)
        print('Digite apenas números válidos.')
        continue
    sleep(4)

    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
        continue

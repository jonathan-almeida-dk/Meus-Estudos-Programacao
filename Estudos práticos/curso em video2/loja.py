import os 
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        produto = float(input('Qual o valor gasto? R$'))
        break # Sai do loop se o valor for numérico
    except ValueError:
       print('Erro! Por favor, digite um valor numérico válido(ex: 150,10.25,0.25)') 


while True:
    print('''FORMAS DE PAGAMENTO:
[1] à vista, dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão sem juros
[4] 3x ou mais no cartão: 20% de juros''')
    try:  
        opcao = int(input('Escolha opção de pagamento: '))
        if 1<= opcao <= 4:
            break # Sai do loop se a opçao for válida
        else:
            print('\nOPÇÃO INVÁLIDA! Por favor, escolha entre 1 e 4.')
    except ValueError:
        print('\nErro! Digite apenas o NÚMERO da opção.')

# A partir daqui, o código só executa se a opção for correta
if opcao == 1:
    total = produto - (produto * 10 / 100)
elif opcao == 2:
    total = produto - (produto * 5 / 100)
elif opcao == 3:
    total = produto
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif opcao == 4:
    total = produto * 1.20
    while True:
        try:
            total_parc = int(input('Quantas parcelas? '))
            if total_parc >= 3:
                break
            else:
                print('Para esta opção, o parcelamento deve ser em 3x ou mais.')
        except:
            print('Erro! Digite um número interio de parcelas.')
    parcela = total / total_parc
    print(f'Sua compra será parcelada em {total_parc}x de R${parcela:.2f} COM JUROS.')
else:
    total = produto
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print(f'Sua compra de R${produto:.2f} vai custar R${total:.2f} no final.')
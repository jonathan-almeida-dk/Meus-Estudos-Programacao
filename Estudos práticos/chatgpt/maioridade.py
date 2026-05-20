from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1,8):
    nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu: '))
    idade = ano_atual - nasc
    if idade > 18:
        maior +=1
    else:
        menor += 1
print(f'Ao todo tem {maior} pessoas maiores de idade.')
print(f'Ao todo tem {menor} pessoas menores de idade.')
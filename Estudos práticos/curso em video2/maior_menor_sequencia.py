maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:  #Se o peso atual for maior do que o guardado na variável 'maior', a variável se atualiza com esse novo valor.
            maior = peso
        if peso < menor:  #Se o peso atual for menor do que o guardado na variável 'menor', a variável se atualiza com esse novo valor.
            menor = peso
print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')

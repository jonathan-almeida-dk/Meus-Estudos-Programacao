soma = 0
cont= 0
for c in range(1, 501, 2): # 1 a 500 sendo multiplos de 3
   if c % 3 == 0: # se o resto da divisao entre 'c' e '3' for igual a 0, execute o restante.
        cont = cont + 1 # conta quantos números foram lidos pelo for
        soma = soma + c # soma cada número dentro da variável 'c' com os requisitos do 'for' de 1 a 500 sendo multiplos de 3
print(f"A soma de todos os {cont} valores solicitados é {soma}.")
    
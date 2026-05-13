soma = 0 # variável para somar os números digitados
cont = 0 # variável para contar os números digitados
for c in range(1, 7): #crie um intervalo de 1 a 6
    n = int(input(f"Digite o {c}º número: "))
    if n % 2==0: # diferencia os ímpares dos pares, só quero os pares neste caso
        soma += n # soma = soma + n
        cont += 1 # cont = cont + 1
print(f"Você informou {cont} números PARES e a soma foi {soma}. ")
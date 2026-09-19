#EXEMPLO SIMPLES DE SOMA

x = int(input("Dê um valor ao x: "))
y = int(input("Agora dê um valor a y: "))


print("A soma de X + Y é:", x + y)

#ou

#EXEMPLO DE USAR CHAVES E DESIGNAR SEQUENCIALMENTE NA ORDEM DELAS.

x = int(input("Digite valor: "))
y = int(input("Digite outro valor: "))
z = x + y

print('A soma de {} e {} é {}!'. format(x, y, z))

#ou

#EXEMPLO DE USAR F-STRINGS

x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
z = x + y

print(f"A soma de {x} e {y} é {z}!")
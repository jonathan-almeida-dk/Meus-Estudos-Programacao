titulo = "TABUADA COM FOR"
print(titulo.center(50,"-"))

n = int(input("Digite um número para ver sua tabuada: "))

for c in range(1,11):
    print(f'{n} x {c} = {n*c}')
idade = int(input("Quantos anos você tem? "))
idade_maior = idade + 10 
print(f"Daqui a 10 anos você terá {idade_maior} anos.")

def maior_idade():
    if idade_maior >= 18:
        print('\nVocê será um adulto(a)!')
    else:
        print('\nVocê ainda será menor de idade!')

maior_idade()

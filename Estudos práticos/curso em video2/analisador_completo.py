soma_idade = 0
maior_idade = 0
mulher_menor = 0
nome_velho = ''

for p in range(1,5):
    print(f' {p} PESSOA '.center(30, '='))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma_idade += idade
    media_idade = soma_idade / 4

    # DESCOBRE QUAL HOMEM É MAIS VELHO E SEU NOME  
    if p == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome

    # DESCOBRE QUANTAS MULHERES SÃO MENORES DE 20 ANOS
    if idade < 20 and sexo in 'Ff':
            mulher_menor += 1


print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
print(f'O homem mais velho tem {maior_idade} anos e seu nome é {nome_velho}.')
print(f'Ao todo são {mulher_menor} mulheres com menos de 20 anos.')
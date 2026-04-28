import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

frase = 'Curso em Video Python'

print(frase[::2])

print(frase.find('Curso'))

print(frase.count('o'))
print(frase.upper().count('O'))

print(len(frase))
print(len(frase.strip()))

frase.replace('Python', 'Android') #AQUI ELE NÃO SALVA, ELE FAZ A ALTERAÇÃO NO MOMENTO QUE LÊ O CÓDIGO, MAS NÃO SALVA
frase = frase.replace('Python', 'Android')#AQUI ELE SALVA A INFORMAÇÃO DE SUBSTITUIR AS PALAVRAS
print(frase.replace('Python', 'Android'))
#FRASES SÃO IMUTÁVEIS A MENOS QUE EU CRIE UMA FUNÇÃO COM ATRIBUIÇÃO PARA ELA IGUAL MOSTRADO ACIMA 👆.

dividido = frase.split()
print(frase.split())
print(dividido[0])# ele mostra a primeira palavra da lista 'dividido'
print(dividido[2][3])# SIGNIFICA QUE É PRA ELE SELECIONAR O ITEM '2' DA LISTA(QUE É A PALAVRA "Video") E A 3ª LETRA QUE É "e", POIS SEMPRE COMEÇA DO ZERO

print(frase.lower())
print(frase.capitalize())
print(frase.title())
print('😎'.join(dividido))
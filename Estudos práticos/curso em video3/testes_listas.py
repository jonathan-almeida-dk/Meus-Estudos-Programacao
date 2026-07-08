num = [1,3,4,5]
num[2] = 10
num.append(7) #adiciona um item ao final da lista
num.sort(reverse=True) #ordena de trás pra frente
num.sort()# ordena em ordem crescente (númerica ou alfabética)
num.insert(2,0) # inseri na posição '2' o item '0'
# num.pop(2) # deleta na posição '2'
num.remove(10) # deleta somente o primeiro item (10 neste caso), se houver repetição, será ignorado.

if 45 in num: # condição para remover todos os itens mesmo sendo repetidos
    num.remove(45)
else:
    print('Não encontrei o número 45')

print('='*40)
print(num)
print(f'Essa lista tem {len(num)} elementos.') # verifica a quantidade de itens na lista
print('='*40)

for c, n in enumerate(num): # mudando tipo de visualização
    print(f'Na posição {c} encontrei o valor {n}...')
print('Final da lista')
print('='*40)

valores = list() # método para criar lista em uma variável
for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) # adicionando através de input
print('='*40)
for c, v in enumerate(valores): # mudando tipo de visualização
    print(f'Na posição {c} encontrei o valor {v}...')
print('Final da lista')
print('='*40)

a = [2,3,4,7]
b = a # isso cria um laço entre as duas listas A e B, se alterar em uma, a outra também será modificada
b = a[:] # isso cria uma cópia de A em B, assim dá pra alterar em uma sem mexer na outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
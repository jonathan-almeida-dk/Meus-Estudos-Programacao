dados = []
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)

print(dados[0]) # Pedro
print(dados[1]) # 25
print('-='*60)

#====================================

pessoas = []

pessoas.append(dados[:]) # cria um cópia com [:] e  adiciona essa cópia da lista, dentro da outra com todos os itens(dá pra fazer várias listas dentro de uma)

pessoas = [['Pedro', 25], ['Maria',19], ['João', 32]]
# CADA LISTA VAI TER 1 ÍNDICE(  << PEDRO, 25 = ÍNDICE '0' >>   << MARIA, 19 = ÍNDICE '1' >>     << JOÃO, 32 = ÍNDICE '2' >>  )
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1])    # ['Maria', 19]
print('-='*60)

#====================================

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')
print('-='*60)

#====================================

galera = []
dado = []
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int((input('Idade: '))))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('-='*60)


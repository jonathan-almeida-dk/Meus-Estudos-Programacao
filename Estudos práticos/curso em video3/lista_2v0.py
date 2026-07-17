dados = []
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)

print(dados[0]) # Pedro
print(dados[1]) # 25

#====================================

# pessoas = []
# pessoas.append(dados[:]) # adiciona uma lista dentro da outra com todos os itens(dá pra fazer várias listas dentro de uma)

# OU

pessoas = [['Pedro', 25], ['Maria',19], ['João', 32]]
# CADA LISTA VAI TER 1 ÍNDICE(  << PEDRO 25 = ÍNDICE '0' >>   << MARIA 19 = ÍNDICE '1' >>     << JOÃO 32 = ÍNDICE '2' >>  )
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1])    # ['Maria', 19]
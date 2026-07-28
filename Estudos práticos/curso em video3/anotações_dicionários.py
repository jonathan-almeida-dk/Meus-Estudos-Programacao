# TUPLAS ()
# LISTAS [] or variavel = list()
# DICIONÁRIOS {} or variavel = dict()
dados = {'nome':'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)

    # Resultado:
    # Pedro
    # 25
    # {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
    # {'nome': 'Pedro', 'sexo': 'M'}

print('='*80)
print('='*80)
#=====================================================================
filme = {'título': 'Star Wars',
         'ano': 1977,
         'Diretor':'George Lucas'
}
print(filme.values()) # mostra o conteúdo(valores) de cada índice
print(filme.keys())   # mostra cada índice(chaves) do dicionário
print(filme.items())  # mostra tanto índices quanto os valores

    # Resultado:
    # dict_values(['Star Wars', 1977, 'George Lucas'])
    # dict_keys(['título', 'ano', 'Diretor'])
    # dict_items([('título', 'Star Wars'), ('ano', 1977), ('Diretor', 'George Lucas')])

print('='*80)
print('='*80)
#=====================================================================

for k, v in filme.items():
    print(f'O {k} é {v}.')
    # Resultado:
    #O título é Star Wars.
    # O ano é 1977.
    # O Diretor é George Lucas.

print('='*80)
print('='*80)
#=====================================================================

# locadora = []
# filmes = {{'titulo':'Star Wars',
#           'ano': 1977,
#           'diretor': 'George Lucas'},

#           {'titulo': 'Avengers',
#           'ano':2012,
#           'diretore':'Joss Whedon'}
# }
# locadora.append(filmes)
# print(locadora)

#=====================================================================

pessoas = {'nome': 'Jonathan', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # para usar f-strings ou chamar os conteúdos de dicionários, deve-se sempre usar >> ASPAS DUPLAS <<
    #RESULTADO:
    # O Jonathan tem 22 anos.
for k in pessoas.keys():
    print(k)
    #RESULTADO:
    # nome
    # sexo
    # idade
print('='*80)
for v in pessoas.values():
    print(v)
    #RESULTADO:
    # Jonathan
    # M
    # 22
print('='*80)
for k, v in pessoas.items():
    print(f'{k} = {v}')
    #RESULTADO:
    # nome = Jonathan
    # sexo = M
    # idade = 22
print('='*80)
pessoas['nome'] = 'Leandro' # ALTERANDO UM ITEM
pessoas['peso'] = 98.5 # ADICIONANDO UM ITEM À BIBLIOTECA
for k, v in pessoas.items():
    print(f'{k} = {v}')
    #RESULTADO:
    # nome = Leandro
    # sexo = M
    # idade = 22
    # peso = 98.5
print('='*80)
print('='*80)
# CRIANDO UMA LISTA COM DICIONÁRIOS
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil[0]) # resultado: {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
print(brasil[1]) # resultado: {'UF': 'São Paulo', 'Sigla': 'SP'}
print(brasil[1]['UF']) # resultado: São Paulo
print(brasil[1]['Sigla']) # resultado: SP
print('='*80)
print('='*80)
estados = {}
brasil = []
for c in range(0,3): # Guarda itens a lista Brasil
    estados['uf'] = input('Unidade Federativa: ')
    estados['sigla'] = input('Sigla do Estado: ')
    brasil.append(estados.copy())
for e in brasil: # Mostra o que foi adicionado à lista
    print(e)
    # RESULTADO:
    # {'uf': 'Minas Gerais', 'sigla': 'Mg'}
    # {'uf': 'São Paulo', 'sigla': 'SP'}
    # {'uf': 'Acre', 'sigla': 'AC'}
for e in brasil: 
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
        # RESULTADO:
        # O campo uf tem valor Acre.
        # O campo sigla tem valor AC.
        # O campo uf tem valor Sampa.
        # O campo sigla tem valor SP.
        # O campo uf tem valor parana.
        # O campo sigla tem valor PR.
for e in brasil: 
    for v in e.values():
        print(v, end = ' ')
    print()
        # RESULTADO:
        # acre ac 
        # sampa sp 
        # parana pr 
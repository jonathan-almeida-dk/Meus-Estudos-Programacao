# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros 
# colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da São Paulo.

times = ('Palmeiras','Flamengo','Fluminense','Athletico-PR','Red Bull Bragantino',
         'Bahia','Coritiba','São Paulo','Atlético-MG','Corinthians','Cruzeiro',
         'Botafogo','Vitória','Internacional','Santos','Grêmio','Vasco da Gama',
         'Remo','Mirassol','Chapecoense')

print('=-'*50)
print('20 PRIMEIROS COLOCADOS EM ORDEM'.center(50))
print(times)
print('=-'*50)
print('\nOs 5 primeiros times: \n',times[0:5])
print('=-'*50)
print('\nOs últimos 4 colocados: \n',times[-4:])
print('=-'*50)
print('TIMES EM ORDEM ALFABÉTICA\n'.center(50))
print(sorted(times))
print('=-'*50)
print(f'\nSão Paulo está em {times.index('São Paulo')+1}° lugar.')
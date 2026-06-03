genero = input('Digite seu gênero [M/F]: ').strip().upper()[0] # o [0] pega só a primeira letra da resposta
continuar = 'S'
while genero not in 'MmFf':
        genero = input('Dados incorretos. Tente novamente: ').upper().strip().upper()[0]
print(f'Sexo {genero} registrado com sucesso.')


            




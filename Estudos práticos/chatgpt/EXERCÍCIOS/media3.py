aprovados = 0
reprovados = 0
excelentes = 0
recuperacao = 0

while True:

    nome = input('Digite o nome do aluno: ')

    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    n3 = float(input('Digite a 3ª nota: '))

    media = (n1 + n2 + n3) / 3

    print(f'\nNome do aluno: {nome}')
    print(f'Média do aluno: {media:.1f}')

    if media < 5:
        reprovados += 1
        print('Reprovado')

    elif media < 7:
        recuperacao += 1
        print('Recuperação')

    elif media < 9:
        aprovados += 1
        print('Aprovado')

    else:
        excelentes += 1
        print('Você foi excelente!')

    print('\n===== RELATÓRIO =====')
    print(f'Excelentes: {excelentes}')
    print(f'Aprovados: {aprovados}')
    print(f'Recuperação: {recuperacao}')
    print(f'Reprovados: {reprovados}')

    while True:
        cont = input('\nDeseja continuar? (s/n): ').lower()

        if cont == 's':
            break

        elif cont == 'n':
            print('\nPrograma encerrado.')
            exit()

        else:
            print('Opção inválida! Tente novamente.')
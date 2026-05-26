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

  print(f'Nome do aluno: {nome}')
  print(f'\nMédia do aluno: {media:.1f}')
  if media < 5:
    reprovados += 1
    print('Reprovado')
  elif media < 7:
    recuperacao += 1
    print('Recuperacao')
  elif media < 9:
    aprovados += 1
    print('Aprovado')
  else:
    excelentes += 1
    print('Você foi excelente!')
    
  print(f'Excelentes: {excelentes}')
  print(f'\nAprovados: {aprovados}')
  print(f'\nReprovados: {reprovados}')
  print(f'\nRecuperação: {recuperacao}')
  cont = input('\nDeseja continuar? (s/n) ').upper().lower()
  if cont == 's':
    continue
  elif cont == 'n':
    break
  else:
    print('Opção inválida! ', end='')
    print('Tente novamente')
    continue
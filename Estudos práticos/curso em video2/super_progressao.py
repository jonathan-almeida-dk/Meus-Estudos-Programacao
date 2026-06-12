
print('=-' * 10)
print('GERADOR DE PA'.center(20))
print('=-' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

cont = 1                  # contador de termos
total = 0                 # variável para impor limite de termos por vez 
mais = 10                 # variável inicial com 10 termos 

while mais != 0:          # enquanto 'mais' for diferente de '0' faça isso:
    total += mais         # 'total' recebe o valor da variável 'mais' para iniciar com 10 termos e contar quantos termos foram feitos no total ao fim do programa
    while cont <= total:  # enquanto o contador for menor ou igual ao total:
        print(f'{termo}➡️', end='  ')
        termo += razao    # termo é atualizado somando com a razão
        cont += 1         # contador
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais?: '))
print(f'Total de progressões de {total} termos.')
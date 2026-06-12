
print('=-' * 10)
print('GERADOR DE PA'.center(20))
print('=-' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

cont = 1 #contador para impor um limite de termos na primeira vez
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}➡️', end='  ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais?: '))
print(f'Total de progressões de {total} termos.')


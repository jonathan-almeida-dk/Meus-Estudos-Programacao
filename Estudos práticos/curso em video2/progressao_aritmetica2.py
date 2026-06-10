print('=-' * 10)
print('GERADOR DE PA'.center(20))
print('=-' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1

while cont <= 10:
    print(f' {termo}➡️ ', end='')
    termo += razao
    cont += 1
print(' FIM')
titulo = '10 TERMOS DE UMA PA'
resultado = titulo.center(30,' ')
print('='*30)
print(resultado)
print('='*30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo_termo = termo + (10 - 1) * razao

for t in range(termo, decimo_termo + razao, razao):
    
    print(t, end= ' → ')
print('ACABOU')
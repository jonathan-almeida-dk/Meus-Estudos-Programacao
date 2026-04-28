import os
os.system('cls')

n1 = float(input('Digite a nota: '))
n2 = float(input('Digite a 2ª nota: '))
n3 = float(input('Digite a 3ª nota: '))
n4 = float(input('Digite a 4ª nota: '))
nota = (n1 + n2 + n3 + n4) / 4

print('{:=^40}'.format('MÉDIA ARITMÉTICA'))

if nota>=8:
    print('Tu é foda patrão 😎')

elif nota>=6:
    print('Concraituleichom meu homi 👌')

elif nota>=5:
    print('Passou mais passou raspando hein 😏')

else:
    print('Estuda mais jumentinho petista 🤞🐴')


print('Tua média aritmética é {:.1f}. '.format(nota))

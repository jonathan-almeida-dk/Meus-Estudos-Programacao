import os
import sys #biblioteca para encerrar ações ou o código em si
os.system('cls' if os.name == 'nt' else 'clear')

print('\033[32m=\033[m' * 14)
print('\033[1:30:42mMédia Do Aluno\033[m')
print('\033[32m=\033[m' * 14)

    
n1 = float(input('Qual a nota da primeira prova?: '))
n2 = float(input('Qual a nota da segunda prova?: '))
media = (n1 + n2) / 2

if n1 or n2 > 10:
    print('Você digitou um valor acima do limite! Tente novamente.')
    sys.exit()#encerra o programa

if media <= 4.9:
    print(f'Tirando notas {n1} e {n2}, a média do aluno é {media}!')
    print('Você se saiu mal, \033[31mREPROVADO\033[m!')
elif media <= 8:
    print(f'Tirando notas {n1} e {n2}, a média do aluno é {media}!')
    print('Você se saiu bem, \033[32mAPROVADO\033[m!')
else:
    print(f'Tirando notas {n1} e {n2}, a média do aluno é {media}!')
    print('Você foi execelente, \033[32mAPROVADO\033[m!👏')

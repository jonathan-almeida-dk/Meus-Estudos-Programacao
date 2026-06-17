print('-'*30)
print('TRATANDO VÁRIOS VALORES')
print('-'*30)

num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    cont +=1
print(f'Você digitou {cont -1} vezes. A soma total é {soma - 999}.')
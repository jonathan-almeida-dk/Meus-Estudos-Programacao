import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

num = int(input('Me diga um número qualquer: '))
res = num % 2
if res == 0:
    print('O número {} é Par!'.format(num))
else:
    print('O número {} é Impar!'.format(num))
    
import os
os.system('cls' if os.name == 'nt' else 'clear')

s1 = float(input("1° SEGMENTO: "))
s2 = float(input('2° SEGMENTO: '))
s3 = float(input('3° SEGMENTO: '))

'''
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('Estes segmentos FORMAM UM TRIANGULO!')
    if s1 == s2 == s3:
        print('Esse triângulo é \033[1;30;41mEQUILÁTERO\033[m!')
    if s1 != s2 != s3 != s1:
        print('Esse triângulo é \033[1;30;46mESCALENO\033[m!')
    else:
        print('Esse triângulo é \033[1;30;42mISÓSCELES\033[m!') 
else:
    print('Estes segmentos NÃO FORMAM UM TRIANGULO!')

'''

# OR


if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Estes segmentos FORMAM UM TRIANGULO ',end='')
    if s1 == s2 == s3:
        print('\033[1;30;41mEQUILÁTERO\033[m!')
    elif s1 != s2 and  s1 != s3 and s2 != s3:
        print('\033[1;30;46mESCALENO\033[m!')
    else:
        print('\033[1;30;42mISÓSCELES\033[m!') 
else:
    print('\033[1;31mEstes segmentos NÃO FORMAM UM TRIANGULO!\033[m')
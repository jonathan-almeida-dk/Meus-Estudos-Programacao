#MÉTODO MATEMÁTICO COMUM PARA CALCULAR HIPOTENUSA
'''co= float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print (' A hipotenusa vai medir {:.2f}'.format(hi))'''


#MESMO MÉTODO COM BIBLIOTECA PARA CALCULAR HIPOTENUSA
'''import math
co= float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = math.hypot(co, ca)
print(' A hipotenusa vai medir {:.2f}'.format(hi))'''


#MÉTODO FROM(É NECESSÁRIO LEMBRAR DE TIRAR O CÓDIGO >>(math.hypot)<<)
from math import hypot
co= float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co, ca)
print(' A hipotenusa vai medir {:.2f}'.format(hi))



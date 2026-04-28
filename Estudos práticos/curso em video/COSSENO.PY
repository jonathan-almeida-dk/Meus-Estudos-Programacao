import os
clear = os.system ('cls' if os.name == 'nt' else 'clear')

'''from math import sin, cos, tan, radians
an = float(input(' Digite o ângulo em graus: '))
an_rad = radians(an)

seno = sin(an_rad)
coss = cos(an_rad)
tang = tan(an_rad)
print(' O seno de {}° é {:.2f} \n O cosseno de {}° é {:.2f} \n A tangente de {}° é {:.2f}'.format(an, seno, an, coss, an, tang))
'''

'''import math 
an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
coss = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(an, sen))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(an, coss))
print('O ângulo de {}° tem o TANGENTE de {:.2f}'.format(an, tang))
'''

from math import sin, cos, tan, radians 
an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print(f'O ângulo de {an}° tem o SENO de {sen:.2f}')
print(f'O ângulo de {an}° tem o COSSENO de {coss:.2f}')
print(f'O ângulo de {an}° tem o TANGENTE de {tang:.2f}')
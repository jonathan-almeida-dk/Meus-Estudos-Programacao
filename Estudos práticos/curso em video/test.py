from math import sin, cos, tan, radians

an = float(input('Digite o ângulo (em graus): '))
# Converter o ângulo de graus para radianos antes de usar as funções
an_rad = radians(an) 

seno = sin(an_rad) # Chamar a função com o ângulo em radianos
coss = cos(an_rad) # Chamar a função com o ângulo em radianos
tang = tan(an_rad) # Chamar a função com o ângulo em radianos

print('O seno de {}° é {:.2f}'.format(an, seno))
print('O cosseno de {}° é {:.2f}'.format(an, coss))
print('A tangente de {}° é {:.2f}'.format(an, tang))

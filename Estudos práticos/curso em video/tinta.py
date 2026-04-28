import os
clear = os.system ('cls' if os.name == 'nt' else 'clear')

A = float(input('Em metros digite a altura da parede: '))
L = float(input('Em metros digite a largura da parede: '))
M = A*L
T = M / 2
print('Com altura e largura de {}m e {}m respectivamente você tem {:.2f}m²'.format(A, L, M))
print('Para pintar essa parede você vai precisar de {:.1f}l de tinta'.format (T))

#Nesse exemplo cada litro de tinta pinta 2m²
#import math
import emoji

'''from math import trunc

num = float(input('Digite um número: '))
print('O número {} e sua porção é inteira {}'.format(num,trunc(num)))'''

# se voce usar o botão de aspas 3 vezes no começo e fim do código ele vira comentário!!
#se for usar import math e não usar o from, obrigatoriamente se usa >> .format(num,math.trunc(num)) <<

num = float(input('Digite um número: '))
print(emoji.emojize(f'O número digitado foi {num} e sua porção inteira é {int(num)} 👍'))

#AS VEZES NÃO PRECISA IMPORTAR MÓDULOS PARA FAZER DETERMINADAS FUNÇÕES, MEMORIZEEE!!!
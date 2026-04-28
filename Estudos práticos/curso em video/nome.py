import os
clear = os.system('cls')

clear

nome = str(input('qual seu nome: ')).strip()
print('Seu nome tem Silva?\nResposta: {}'.format('silva' in nome.lower()))
#ESTE COMANDO FAZ COM QUE ELE IDENTIFIQUE SE TEM O NOME SILVA EM QUALQUER LUGAR DO NOME.
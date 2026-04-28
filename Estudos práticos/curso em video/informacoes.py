import os
clear = os.system('cls')

palavra = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(palavra))
print('É alfanumérico?: ', palavra.isalnum())
print('É alfabético?: ', palavra.isalpha())
print('É um caracter comum?: ', palavra.isascii())
print('É um decimal?: ', palavra.isdecimal())
print('É um digito númerico?: ', palavra.isdigit())
print('É um identificador?: ', palavra.isidentifier())
print('Está tudo em minúsculo?: ', palavra.islower())
print('É printável(imprimível)?: ', palavra.isprintable())
print('É um espaço em branco?: ', palavra.isspace())
print('Está em formato de título?: ', palavra.istitle())
print('Está tudo maiúsculo?: ', palavra.isupper())

import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

clear
cidade = str(input('Em que cidade você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')
#ESTE COMANDO SÓ ACEITARÁ QUE A PESSOA MORE EM UMA CIDADE COM O NOME SANTO;
#O .upper == 'SANTO' FAZ COM QUE ELE TRANSFORME OS CARACTERES PARA QUE MESMO SE DIGITAR ERRADO, DARÁ O RESULTADO ESPERADO.
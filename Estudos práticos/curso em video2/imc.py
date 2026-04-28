import os 
os.system('cls' if os.name == 'nt' else 'clear')
'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule seu Índice de Massa Corporal (IMC) e mostre seu status'''

peso = float(input('Qual seu peso(Kg)?: '))
altura = float(input('Qual a sua altura(m)?: '))
imc = peso / (altura ** 2) #altura ao quadrado
print(f'Seu IMC é de {imc:.2f}')
if imc <= 18.5:
    print('Você está \033[7;30mABAIXO DO PESO!\033[m Cuidado!')
elif imc <= 25:
    print('Você está no \033[1;32mPESO IDEAL\033[m.')
elif imc <= 30:
    print('Você está com \033[1;31mSOBREPESO\033[m. Preste atenção.')
elif imc <= 40:
    print('Você está \033[7;31;41mOBESO\033[m! Se cuide melhor.')
else:
    print('Você está com \033[1;30;41mOBESIDADE MÓRBIDA\033[m!! Vá se cuidar!')
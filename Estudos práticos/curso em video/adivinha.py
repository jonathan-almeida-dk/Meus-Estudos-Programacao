import os
from random import randint
from time import sleep

clear = os.system('cls' if os.name == 'nt' else 'clear')
adv = randint(0,5)

print('\033[33m-=--\033[m'*20)
print('Vou pensar em um número entre \033[4;31;40m0\033[m e \033[4;31;40m5\033[m. Tente adivinhar...')
print('\033[33m-=--\033[m'*20)


perg = int(input('\033[7;40mEm que número eu pensei?\033[m\033[1;32m '))
sleep(0.5)
print('\033[m\033[1;41mPROCESSANDO...\033[m')
sleep(1.5)

if perg == adv:
    print('\033[42mParabéns. Você acerto mizeravi😍🤞\033[m')
else:
    print('\033[1;31mTu é ruim dmai hahahaha 🤣, eu pensei no número {} e não no {}.\033[m'.format(adv, perg))


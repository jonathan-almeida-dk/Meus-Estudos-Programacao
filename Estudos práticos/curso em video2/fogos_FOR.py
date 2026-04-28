import os
from time import sleep
clear = os.system('cls' if os.name == 'nt' else 'clear')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('KABUM POU POU POU POU')

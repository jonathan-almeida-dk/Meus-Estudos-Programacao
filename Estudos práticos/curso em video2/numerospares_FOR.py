import os
clear = os.system('cls' if os.name == 'nt' else 'clear')

print('inicio')
for c in range(0, 51, 2):
    print(c)
print('fim')
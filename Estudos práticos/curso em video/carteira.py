import os
clear = os.system('cls' if os.name == 'nt' else 'clear' )

dólar = (5.41)
dindin = float(input("Quanto você tem na carteira?\nR$ "))
comprar = dindin / dólar
print(f'Com R${dindin:.2f} você pode comprar U${comprar:.2f}.')


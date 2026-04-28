import os
os.system('cls' if os.name == 'nt' else 'clear')

m = float(input('Digite uma distancia em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m *100
mm = m *1000
print(f'As distancias em {m}m convertidas são: \n {km}km \n {hm}hm \n {dam}dam \n {dm}dm \n {cm}cm \n {mm}mm')
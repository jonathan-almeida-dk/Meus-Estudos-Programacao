from time import sleep

numero = int(input("Diga um número:"))

def par_impar(numero):   
   if numero % 2 == 0:
      print("É par e ")

   else:
      print("É impar e")

def positivo_negativo(numero):
   if numero > 0:
      print('é positivo')
   elif numero < 0:
      print('é negativo')
   else:
      print('é zero')

print("Analisando o número...")
sleep(2)

par_impar(numero)
positivo_negativo(numero)
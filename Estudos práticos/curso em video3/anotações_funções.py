# =============================================

def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

# PROGRAMA PRINCIPAL
título(' CURSO EM VÍDEO '.center(30,'='))
título(' PYTHON É TOP '.center(30,'='))
título(' OLÁ, MUNDO! '.center(30,'='))

# =============================================
print('-'*30)
def soma(a, b): # obrigatório o uso de dois parâmetros
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma é A + B = {s}')

# PROGRAMA PRINCIPAL
soma(b=4,a=5) # 2 parâmetros
soma(7,2)

# ==============================================

print('-'*30)
def contador (*num):
    for valor in num:
        print(f'{valor} ', end='')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
print()
# ==============================================

print('-'*30)
def contador2 (*num): # desempacotamento
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador2(2,1,7)
contador2(8,0)
contador2(4,4,7,6,2)
# ==============================================
print('-'*30)
def dobra(lst): # dobrando valores em lista
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)
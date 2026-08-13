help() # é usado para ler documentos explicativos de qualquer função da linguagem. EX: help(print) help(input) help(datetime) etc...

# -------------------------------------------

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :parâmetro i: início da contagem            <<< #  ISSO SE CHAMA DOCSTRINGS(são usadas para criar "explicações" sobre a função desenvolvida)
    :parâmetro f: fim da contagem               <<< # Para usar basta usar aspas duplas 3 vezes no início e fim com a escrita dentro, no início de cada função
    :parâmetro p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c+=p
    print('FIM!')
help(contador)

print('-='*30)
# -------------------------------------------

        # PARÂMETROS OPCIONAIS
def somar(a=0,b=0,c=0): # quando um parâmetro recebe 0, significa que se quando a função for chamada, e se caso não houver esse terceito parâmetro, ela recebe 0
    s = a+b+c
    print(f'A soma é {s}')

somar(3,2,5)
somar(8,4)
somar() # SE CASO NÃO HOUVER PARÂMETRO NENHUM, ELE SOMA O QUE FOI DEFINIDO NA FUNÇÃO >>( def somar(a=0,b=0,c=0): )<<

print('-='*30)
# -------------------------------------------

            # ESCOPO VARIÁVEIS
# =============================
def teste(b): 
    global a                    # Esse comando diz para não criar uma variável 'a', use a global, sendo assim , a variável global 'a' vale 8 (o valor da variável global deixa de existir)
    a = 8                       # esse A não é o mesmo A do escopo global, esse programa passa a ter 2 variáveis, uma global e outra local                 
    b+=4                        
    c=2                         # ESCOPO LOCAL
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
# =============================
a = 5                           # ESCOPO GLOBAL
teste(a)
print(f'A fora vale {a}')
# =============================
print('-='*30)
# -------------------------------------------
        # RETORNANDO VALORES
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s
r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
print('-='*30)
# -------------------------------------------

# Lê a frase, remove os espaços extras nas pontas e padroniza em maiúsculas
frase = input('Digite uma frase: ').strip().upper()

# Divide a frase em uma lista de palavras usando os espaços como separador
palavras = frase.split()

# Junta todas as palavras da lista em uma única string, eliminando os espaços internos
junto = ''.join(palavras)

# Inicializa uma string vazia para armazenar a frase invertida
inverso = ''

# Loop que vai do índice da última letra até o índice 0, andando de trás para frente
for letra in range(len(junto) - 1, - 1, - 1):
    
    # Adiciona a letra atual à string 'inverso'
    inverso += junto [letra]

# Exibe o resultado da inversão na tela
print(f'O inverso de {junto} é {inverso}.')

# Verifica se a string original sem espaços é igual à sua versão invertida
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')


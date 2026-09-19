# Crie uma função chamada contar_palavras que receba uma frase (string) como argumento.
# A função deve limpar a frase, ignorar letras maiúsculas/minúsculas
# e retornar um dicionário com a contagem de cada palavra.

def contar_palavras(frase):
    # 1. Converter tudo para minúsculas e dividir por espaços
    palavras_brutas = frase.lower().split()
    
    # 2. Limpar a pontuação de cada palavra usando List Comprehension
    palavras_limpas = [palavra.strip(",.!") for palavra in palavras_brutas]
    
    # 3. Montar o dicionário de frequência
    frequencia = {}
    for palavra in palavras_limpas:
        if palavra:  # Evita adicionar strings vazias caso fiquem isoladas
            frequencia[palavra] = frequencia.get(palavra, 0) + 1
            
    return frequencia

# Testando a função
texto_teste = "Python é incrível, sério! Eu amo programar em Python."
print(contar_palavras(texto_teste))

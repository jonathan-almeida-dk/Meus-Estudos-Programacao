# Exercício Python 114: Crie um código em Python que teste
# se o site pudim está acessível pelo computador usado.

import requests

url = 'https://pudim.com.br'

try:
    resposta = requests.get(url, timeout=5)
    if resposta.status_code == 200:
        print(f'O site {url} está acessível!')
    else:
        print(f'O site respondeu, mas com o código de status: {resposta.status_code}')
except requests.exceptions.RequestException:
    print(f'O site {url} NÃO está acessível no momento.')
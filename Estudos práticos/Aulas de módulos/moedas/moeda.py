# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe 
# esse módulo e use algumas dessas funções.

# Exercício Python 108: Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.

# Exercício Python 109: Modifique as funções que foram criadas no desafio 107
# para que elas aceitem um parâmetro a mais, informando se o valor retornado
# por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas
# pelas funções que já temos no módulo criado até aqui.

def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)

def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \tR${moeda(preço) }')
    print(f'Dobro do preço: \tR${dobro(preço, True) }')
    print(f'Metade do preço: \tR${metade(preço, True) }')
    print(f'{taxaa}% de aumento: \tR${aumentar(preço, taxaa, True) }')
    print(f'{taxar}% de redução: \tR${diminuir(preço, taxaa, True) }')
    print('-'*30)


# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.     

def escreva(msg):
    tam = len(msg)
    print('~'*20)
    print(msg)
    print('~'*20)

#  Programa oficial
escreva('Gustavo guanabara')
escreva('Curso de python no youtube')
escreva('Cev')

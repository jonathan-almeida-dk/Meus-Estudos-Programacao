import os
os.system('cls')

n = int(input(' Digite um número: '))
x2 = n * 2
x3 = n * 3
rq = n ** (1/2)
print('{:=^60}'.format('CALCULANDO NÚMEROS'))
print(' O dobro de {} é: {} \n O triplo é: {}\n A raiz quadrada é :{:.0f}'.format(n, x2, x3, rq))
# o uso do \n serve para pular linhas no print
print('{:=^60}'.format('FIM'))
# o uso do {:=^60} serve para centralizar o texto com 60 caracteres de largura, preenchendo com '='
# o uso do ** é para potenciação, no caso a raiz quadrada é a potência de 1/2
# o uso do ^ é para elevar um número a uma potência
# o uso do * é para multiplicação
# o uso do int() é para converter o valor digitado em número inteiro
# o uso do input() é para receber um valor do usuário
# o uso do print() é para exibir uma mensagem na tela
# o uso do import os e os.system('cls') é para limpar a tela no Windows, no Linux use 'clear'
# o uso do format() é para formatar a string, substituindo os {} pelos valores passados como argumentos
# o uso do :.0f é para formatar o número como float com 0 casas decimais
# o uso do :^60 é para centralizar o texto com 60 caracteres de largura

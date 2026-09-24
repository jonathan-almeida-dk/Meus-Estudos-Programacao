class Xadrez():
    def __init__(self):

        self.torre = input('Qual nome da peça que fica nas \nextremidade inferiores do tabuleiro?:\n')
        print('='*50)
        self.cavalo = input('Qual a peça que pode ser montada na vida real?:\n')
        print('='*50)
        self.rei = input('Qual peça é a principal do jogo?:\n')

    def mensagem0(self):
        print(f'A resposta da 1ª pergunta é {self.torre}.')
        print('='*50)

        print(f'A resposta da 2ª pergunta é {self.cavalo}.')
        print('='*50)

        print(f'A resposta da 3ª pergunta é {self.rei}.')
        print('='*50)

x = Xadrez()
print('')
print(' RESPOSTAS '.center(50,'='))
x.mensagem0()


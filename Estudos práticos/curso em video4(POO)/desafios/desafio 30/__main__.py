from HashSenha import *

def main():
    c = Credencial()
    c.senha = input('Digite a sua senha: ')
    print(c.senha)

    c.validar('Gafanhoto')

if __name__ == '__main__':
    main()
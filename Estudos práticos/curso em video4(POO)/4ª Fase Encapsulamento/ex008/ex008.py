class ContaBancaria:
    '''
Cria uma conta bancária e permite fazer saques e depósitos
    '''
    def __init__(self, id, nome, __saldo = 0):
        self.id = id            # público (+)
        self._titular = nome    # protegido (#)
        self.__saldo = __saldo  # privado(-)
        print(f'Conta {self.id} criada com sucesso. __saldo atual de R${self.__saldo:,.2f}')


    def __str__(self):
        # return f'A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo.'
        return f'Estado atual da conta: {self.__dict__}'


    def depositar(self, valor):
        valor = abs(valor) # abs: significa que ele tira o sinal e considera somente o valor numérico
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')


    def sacar(self, valor):
        valor = abs(valor) # abs: significa que ele tira o sinal e considera somente o valor numérico
        if valor > self.__saldo:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id}: __saldo INSUFICIENTE')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')





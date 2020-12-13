class Conta:

    #atributos privados __
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print(self.__class__, self.__numero, self.__titular, self.__saldo, self.__limite)

    @staticmethod
    def codigo_banco():
        return "002"

    @staticmethod
    def codigo_bancos():
        return {"BB": "001", "CEF": "104"}

    def limite_conta(self):
        print(self.__limite)

    def extrato(self):
        print("Saldo atual {} do titular {}.".format(self.__saldo,self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        self.extrato()

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            self.extrato()
        else:
            print("Valor maior do que o permitido!")

    def transferir(self, valor, destino):
        print("Transferindo {} para a Conta {}".format(valor, destino.__numero))
        self.sacar(valor)
        destino.depositar(valor)

    def __pode_sacar(self, valor):
        return valor <= self.__saldo + self.__limite

    #GETTERS
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

if __name__ == "__main__":
    conta1 = Conta("123", "Miskante", 120000.0, 5000000.0)
    conta2 = Conta("1003", "Katruski", 1120000.0, 1000000.0)
    conta1.extrato()
    conta1.depositar(5000)
    conta1.sacar(2500000000000)
    conta1 = Conta("123", "Miskante", 120000.0, 5000000.0)
    #recebendo a referencia do mesmo objeto
    outraConta = conta1
    outraConta.depositar(9999)
    #mesmo valor
    outraConta.extrato()
    conta1.extrato()
    #remove a referencia para para o Objeto
    outraConta = None
    conta1.limite_conta()

    conta4 = Conta("0004", "aaa", 100, 200)
    conta5 = Conta("0005", "bbb", 100, 200)

    conta4.transferir(30, conta5)

    print(Conta.codigo_banco())
    print(Conta.codigo_bancos())
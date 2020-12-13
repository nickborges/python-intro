class Cliente:
    tamanho_cpf = 11

    def __init__(self, nome):
        self.__nome = nome

    #GETTER
    @property
    def nome(self):
        print("chamando get com @property {}".format(self.__nome.title()))
        return self.__nome.title()

    #SETTER
    @nome.setter
    def nome(self, nome):
        #print("chamando set nome {}".format(nome))
        self.__nome = nome

cliente = Cliente("Fulano")
cliente.nome
cliente.nome = "Mudou_de_nome"
cliente.nome
print(cliente.tamanho_cpf)
#sempre devemos fechar o arquivo depois de qualquer ação
#w = apaga e escreve, a = adiciona mais texto
#a forma antiga de fazer era sem o with, porém era necessário fechar o arquivo. com with o close() é feito automagicamente.

def escrever_aquivo():
    print(">>>escrever_arquivo<<<")
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write("primeira palavra\n")
        arquivo.write("segunda palavra\n")
    print("")

def ler_arquivo():
    print(">>>ler_arquivo<<<")
    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.read())
        arquivo.close()

    #para ler novamente devemos abri-lo
    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.read())

def ler_primeira_linha_arquivo():
    print(">>>ler_primeira_linha_arquivo<<<")

    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.readline())

def procurar_palavra_arquivo():
    print(">>>procurar_palavra_arquivo<<<")

    with open("arquivo.txt", "r") as arquivo:
        palavra = "segunda" in arquivo.read()
        print(palavra)


if(__name__ == "__main__"):
    escrever_aquivo()
    ler_arquivo()
    ler_primeira_linha_arquivo()
    procurar_palavra_arquivo()
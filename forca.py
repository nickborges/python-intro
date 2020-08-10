def jogar():
    print("Bem-vindo ao jogo da forca:")

    enforcou = False
    acertou = False
    palavra = "java"

    while(not enforcou and not acertou):
        letra = input("Informe a Letra:")
        break

if(__name__=="__main__"): #deixa disponível para executar o arquivo apenas quando chamado diretamente, mas não o executa diretamente através de outro arquivo(apenas quando definido).
    jogar()
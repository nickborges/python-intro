import random
def jogar():
    print("Bem-vindo ao jogo de adivinhação:")

    numero_secreto = random.randrange(0,51)
    teste = False

    while (teste == False):
        numero_digitado = int(input("Informe um número:"))
        acertou = numero_digitado == numero_secreto
        maior = numero_digitado > numero_secreto
        menor = numero_digitado < numero_secreto

        if (acertou):
            print("Acertou o número secreto é = ", numero_digitado)
            teste = True
        else:
            if (menor):
                print("Número digitado é menor que o número secreto!")
            elif (maior):
                print("Número digitado é maior que o número secreto!")
if(__name__=="__main__"): #deixa disponível para executar o arquivo diretamente, mas não executa diretamente(sem definir) através de outro arquivo.
    jogar()
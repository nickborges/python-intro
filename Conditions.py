numero_secreto = 42

# < - menor que
# > - maior que
# <= - menor ou igual a
# >= - maior ou igual a
# == - igual a
# != - diferente de

def executa():
    teste = False

    while(teste == False):
        numero_digitado = int(input("Informe um número:"))
        acertou = numero_digitado == numero_secreto
        maior = numero_digitado > numero_secreto
        menor = numero_digitado < numero_secreto

        if(acertou):
            print("Acertou o número secreto é = ", numero_digitado)
            teste = True
        else:
            if(menor):
                print("Número digitado é menor que o número secreto!")
            elif(maior):
                print("Número digitado é maior que o número secreto!")
executa()
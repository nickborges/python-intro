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

def teste_for():
    print("teste_for")
    for count in range(1, 10):
        print(count)
teste_for()

def teste_for_step():
    print("teste_for_step")
    for count in range(0, 10, 2):
        print(count)
teste_for_step()

def teste_for_manual():
    print("teste_for_manual")
    for count in [1,2,3,4,5]:
        print(count)
teste_for_manual()

def teste_for_break():
    print("teste_for_break")
    for count in range(1, 10, 2):
        if(count == 3):
            print(count)
            break
teste_for_break()
# > - maior que
# <= - menor ou igual a
# >= - maior ou igual a
# == - igual a
# != - diferente de
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
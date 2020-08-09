numero_secreto = 42

numero_digitado = input("Informe um número:")

if(numero_secreto == int(numero_digitado)):
    print("Número secreto = ", numero_digitado)
else:
    print("Número errado!")
    print("O número certo era:", numero_secreto)
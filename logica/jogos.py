from logica import forca, adivinhacao

escolha = int(input("Informe (1) para Forca e (2) par Adivinhação:"))

if (escolha == 1):
    forca.jogar()
elif (escolha == 2):
    adivinhacao.jogar()
else:
    print("Escolha uma opção válida!")

# print
nome = "Fulano"
idade = 19
print("param 1", "param 2", "param3", 4, "5", 6, sep="-")
print("param 1", "param 2", "param3", 4, "5", 6, sep=", ")
print("param 1", "param 2", "param3", 4, "5", 6, sep="\n")
print("param 1", "param 2", "param3", 4, "5", 6, end="\n")
print(f'olá {nome} você tem quanto anos? {idade}')

# Ttipos
## Uma variável só passa a existir quando atribuímos um valor
## Convenção o padrão Snake_Case
nome = "String Nome"
idade = 22

print(type(nome))
print(type(idade))
##
teste = "AAA"
print(type(teste)) #str
teste = 10
print(type(teste)) #int
teste = 5.3
print(type(teste)) #float
##
idade_pessoa = 23
nome_pessoa = "String aqui"

# Input
def funcao_teste():
    nome = input('Qual seu nome? ')
    print(f'Olá {nome}')

funcao_teste()

def funcao_com_parametros(param1):
    print(param1)

#def funcao_com_parametros(param1, param2): #não existe sobre carga(Overloading)
#    print(param1, param2)

funcao_com_parametros("Parâmetro 1")
#funcao_com_parametros("Teste", 10)
# Numérico
numero_decimal = 11/3
print(numero_decimal)
print(type(numero_decimal))

string_b = "10"
inteiro_b = 10
# print(string_b + inteiro_b) ##TypeError: can only concatenate str (not "int") to str
print(int(string_b) + inteiro_b)

numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto) #20202020202020202020

# String
string_a = "Recebe um str"
print(string_a)
string_c = "CCC"
string_d = "DDD"
print(string_c + string_d) #CCCDDD
print(string_c, string_d) #CCC DDD
print(string_c, string_d, sep="") #CCCDDD
string_a = "Recebe um str"

# String interpolation
string_e = "Teste {} recebe o valor {}".format(1, "parangaricutirimirruaro")
print(string_e)

string_f = "Testando a string"
print(f"Imprime aqui {string_f}")

# Format
string_format1 = "R$ {:f}".format(1.89)
print(string_format1)

string_format2 = "R$ {:.2f}".format(1.8999) #coloca 2 casas decimais
print(string_format2)

string_format3 = "R$ {:7.2f}".format(123.99) #coloca espaços na fentre do número
print(string_format3)

string_format4 = "R$ {:08.2f}".format(12.99) #coloca zeros a esquerda
print(string_format4)


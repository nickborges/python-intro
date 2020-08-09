string_a = "Recebe um str"
print(string_a)

string_b = "10"
inteiro_b = 10
# print(string_b + inteiro_b) ##TypeError: can only concatenate str (not "int") to str
print(int(string_b) + inteiro_b)

numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto) #20202020202020202020

string_c = "CCC"
string_d = "DDD"
print(string_c + string_d) #CCCDDD
print(string_c, string_d) #CCC DDD
print(string_c, string_d, sep="") #CCCDDD
### Documentação
https://docs.python.org/pt-br/3/tutorial/index.html

#### Python 2 vs Python 3
* Python2
  * raw_input(...) recebe os dados de entrada sempre como string, mesmo informando um inteiro.
  * input(...) recebe os dados de entrada e converte para o tipo, caso informado um inteiro já faz a conversão.
  * print(...) nao tem os parâmetro sep="" e end="" por exemplo
  * Em uma função o parênteses é opcional, exemplo: print "alguma coisa" ou print("alguma coisa")
* Python 3
  * raw_input(...) não existe mais. 
  * input(...) recebe os dados de entrada sempre como string.
  * print(...) tem os novos parâmetros como sep="" e end="".
  * int(...) existem no Python 3.
  * Em uma função o parênteses é obrigatório.
### Documentação
https://docs.python.org/pt-br/3/tutorial/index.html
https://docs.python.org/3.8/library/index.html
https://docs.python.org/3.8/reference/index.html

#### Funções built-in
* Já estão disponíveis no Python e podem ser chamadas em todo lugar do nosso código.
* Random não é uma função built-in e precisa ser importada.

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
  
#### Funções Built-in
https://docs.python.org/3.8/library/functions.html
 
#### String 
https://docs.python.org/3.8/library/text.html

#### Sequence(String, List, Tuple, Range)
* https://docs.python.org/3.8/library/stdtypes.html#sequence-types-list-tuple-range
* https://docs.python.org/3.8/library/stdtypes.html#list
* String: também é considerada uma sequencia.
* list usa colchetes [] para inicialização, tuple usa parênteses ()
* list é mutável, tuple é imutável

#### Set, Dict
* set:
  * https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
  * https://docs.python.org/3.8/library/stdtypes.html#set
* dict: 
  * https://docs.python.org/3.8/library/stdtypes.html#mapping-types-dict 
  * https://docs.python.org/3.8/library/stdtypes.html#dict

#### Escrita e Leitura de Arquivos

#### Getter e Setters
* @property - para get criar o método com o mesmo nome do atributo
* @nomedoatributo.setter - para criar o seter

#### Modificadores de acesso
* private:
  * atributos:
  ```def __init__(self, nome):
        self.__nome = nome
  ```
  * métodos:
  ```
    def __nome_do_metodo(self, parametro)
  ```
* static:
    * métodos:
    ```
    @staticmethod
    def codigo_banco():
        return "002"
    ```
* métodos de classe:
  * acessar estes métodos de dentro dos métodos de instância.
  ```
  class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'
  ```

#### Herança
```
class Veiculo:
    def abastecer(self, litros):
        print(litros)

class Moto(Veiculo):
    super().__init__(40)
    
class Carro(Veiculo):
    super().__init__(45)
```

# Funções embutidas nativas do python (Built-in):
# São funções que já vêm carregadas no Python
# e ficam disponíveis globalmente durante a execução do programa.
# Fazem parte do conjunto básico de ferramentas da linguagem.

#-----//--------//------------//----------//----------//-----------//---------//

# ==============================================================
# Esta lista abaixo contém apenas funções carregadas automaticamente
# pelo runtime do Python no namespace global "builtins".
# Não inclui funções vindas de módulos como:
# math, random, datetime etc.
# ==============================================================


# region | abs()
# ==============================================================
# abs()
# Retorna o valor absoluto de um número.
# ==============================================================

print(abs(-10))
# endregion


# region | aiter()
# ==============================================================
# aiter()
# Cria um iterador assíncrono.
# ==============================================================

# async_iterador = aiter(objeto_assincrono)
# endregion


# region | all()
# ==============================================================
# all()
# Retorna True se todos os elementos forem verdadeiros.
# ==============================================================

print(all([True, True, True]))
# endregion


# region | anext()
# ==============================================================
# anext()
# Retorna o próximo valor de um iterador assíncrono.
# ==============================================================

# valor = await anext(iterador_assincrono)
# endregion


# region | any()
# ==============================================================
# any()
# Retorna True se pelo menos um elemento for verdadeiro.
# ==============================================================

print(any([False, False, True]))
# endregion


# region | ascii()
# ==============================================================
# ascii()
# Retorna representação ASCII de um objeto.
# ==============================================================

print(ascii("Olá"))
# endregion


# region | bin()
# ==============================================================
# bin()
# Converte inteiro para binário.
# ==============================================================

print(bin(10))
# endregion


# region | bool()
# ==============================================================
# bool()
# Converte valor para booleano.
# ==============================================================

print(bool(1))
# endregion


# region | breakpoint()
# ==============================================================
# breakpoint()
# Inicia depuração.
# ==============================================================

# breakpoint()
# endregion


# region | bytearray()
# ==============================================================
# bytearray()
# Cria coleção mutável de bytes.
# ==============================================================

print(bytearray(b"abc"))
# endregion


# region | bytes()
# ==============================================================
# bytes()
# Cria coleção imutável de bytes.
# ==============================================================

print(bytes("abc", "utf-8"))
# endregion


# region | callable()
# ==============================================================
# callable()
# Verifica se objeto pode ser chamado.
# ==============================================================

print(callable(print))
# endregion


# region | chr()
# ==============================================================
# chr()
# Converte código Unicode em caractere.
# ==============================================================

print(chr(65))
# endregion


# region | classmethod()
# ==============================================================
# classmethod()
# Define método ligado à classe.
# ==============================================================

class Pessoa:

    nome = "Carlos"

    @classmethod
    def mostrar_nome(cls):
        print(cls.nome)
# endregion


# region | compile()
# ==============================================================
# compile()
# Compila código-fonte.
# ==============================================================

código = compile("print(2 + 2)", "teste", "exec")
# endregion


# region | complex()
# ==============================================================
# complex()
# Cria número complexo.
# ==============================================================

print(complex(2, 3))
# endregion


# region | delattr()
# ==============================================================
# delattr()
# Remove atributo de objeto.
# ==============================================================

class Teste:
    atributo = 10

delattr(Teste, "atributo")
# endregion


# region | dict()
# ==============================================================
# dict()
# Cria dicionário.
# ==============================================================

print(dict(nome="Carlos"))
# endregion


# region | dir()
# ==============================================================
# dir()
# Lista atributos/métodos.
# ==============================================================

print(dir(str))
# endregion


# region | divmod()
# ==============================================================
# divmod()
# Retorna divisão inteira e resto.
# ==============================================================

print(divmod(10, 3))
# endregion


# region | enumerate()
# ==============================================================
# enumerate()
# Retorna um iterador que produz pares (índice, valor) ao percorrer um iterável.
# ==============================================================

nomes = ["Ana", "João", "Carlos"]

for indice, nome in enumerate(nomes, start=1):
    print(indice, nome)
# endregion


# region | eval()
# ==============================================================
# eval()
# Executa expressão dinamicamente.
# ==============================================================

print(eval("2 + 2"))
# endregion


# region | exec()
# ==============================================================
# exec()
# Executa bloco de código dinamicamente.
# ==============================================================

exec("print('Olá')")
# endregion


# region | filter()
# ==============================================================
# filter()
# Retorna um iterador com os elementos do iterável verificado que passam pelo teste informado.
# ==============================================================

pares = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])

print(list(pares))
# endregion


# region | float()
# ==============================================================
# float()
# Converte/cria um número de ponto flutuante (float).
# ==============================================================

print(float("3.14"))
# endregion


# region | format()
# ==============================================================
# format()
# Formata valores.
# ==============================================================

print(format(10, "b"))
# endregion


# region | frozenset()
# ==============================================================
# frozenset()
# Cria conjunto imutável.
# ==============================================================

print(frozenset([1, 2, 3]))
# endregion


# region | getattr()
# ==============================================================
# getattr()
# Obtém atributo dinamicamente.
# ==============================================================

print(getattr(str, "upper"))
# endregion


# region | globals()
# ==============================================================
# globals()
# Retorna o dicionário que representa o namespace global atual.
# ==============================================================

print(globals())
# endregion


# region | hasattr()
# ==============================================================
# hasattr()
# Verifica existência de atributo.
# ==============================================================

print(hasattr(str, "upper"))
# endregion


# region | hash()
# ==============================================================
# hash()
# Retorna hash do objeto.
# ==============================================================

print(hash("abc"))
# endregion


# region | help()
# ==============================================================
# help()
# Exibe documentação.
# ==============================================================

# help(print)
# endregion


# region | hex()
# ==============================================================
# hex()
# Converte para hexadecimal.
# ==============================================================

print(hex(255))
# endregion


# region | id()
# ==============================================================
# id()
# Retorna identidade lógica do objeto.
# ==============================================================

print(id(10))
# endregion


# region | input()
# ==============================================================
# input()
# Recebe entrada do usuário.
# sempre retorna uma string, se o objetivo for utilizar o dado inserido para cálculo, será necessário conversão. 
# Para tal veja as builtin defs "int(), float()" etc.
# ==============================================================

# nome = input("Digite seu nome: ")
# endregion


# region | int()
# ==============================================================
# int()
# Converte para inteiro.
# ==============================================================

print(int("10"))
# endregion


# region | isinstance()
# ==============================================================
# isinstance()
# Verifica tipo do objeto.
# ==============================================================

print(isinstance(10, int))
# endregion


# region | issubclass()
# ==============================================================
# issubclass()
# Verifica herança entre classes.
# ==============================================================

print(issubclass(bool, int))
# endregion


# region | iter()
# ==============================================================
# iter()
# Cria iterador.
# ==============================================================

iterador = iter([1, 2, 3])
# endregion


# region | len()
# ==============================================================
# len()
# Retorna tamanho.
# ==============================================================

print(len([1, 2, 3]))
# endregion


# region | list()
# ==============================================================
# list()
# Cria lista.
# ==============================================================

print(list((1, 2, 3)))
# endregion


# region | locals()
# ==============================================================
# locals()
# Retorna um mapping que representa o namespace local atual.
# ==============================================================

print(locals())
# endregion


# region | map()
# ==============================================================
# map()
# Retorna um iterador que aplica uma função aos elementos de um ou mais iteráveis.
# ==============================================================

def dobrar(numero):
    return numero * 2

numeros = [1,2,3]

resultado = map(dobrar, numeros)

print[(list(resultado))]
# endregion


# region | max()
# ==============================================================
# max()
# Retorna maior valor.
# ==============================================================

print(max([1, 2, 3]))
# endregion


# region | memoryview()
# ==============================================================
# memoryview()
# Cria visão direta da memória.
# ==============================================================

dados = memoryview(b"abc")
# endregion


# region | min()
# ==============================================================
# min()
# Retorna menor valor.
# ==============================================================

print(min([1, 2, 3]))
# endregion


# region | next()
# ==============================================================
# next()
# Retorna próximo elemento.
# ==============================================================

print(next(iter([1, 2, 3])))
# endregion


# region | object()
# ==============================================================
# object()
# Classe base do Python.
# ==============================================================

obj = object()
# endregion


# region | oct()
# ==============================================================
# oct()
# Converte para octal.
# ==============================================================

print(oct(10))
# endregion


# region | open()
# ==============================================================
# open()
# Abre arquivos.
# ==============================================================

# arquivo = open("teste.txt", "r")
# endregion


# region | ord()
# ==============================================================
# ord()
# Retorna código Unicode.
# ==============================================================

print(ord("A"))
# endregion


# region | pow()
# ==============================================================
# pow()
# Potência matemática.
# ==============================================================

print(pow(2, 3))
# endregion


# region | print()
# ==============================================================
# print()
# Exibe na tela.
# ==============================================================

print("Olá")
# endregion


# region | property()
# ==============================================================
# property()
# Cria atributo controlado.
# ==============================================================

class Produto:

    def __init__(self):
        self._preco = 0

    @property
    def preco(self):
        return self._preco
# endregion


# region | range()
# ==============================================================
# range()
# Gera sequência numérica.
# ==============================================================

for numero in range(3):
    print(numero)
# endregion


# region | repr()
# ==============================================================
# repr()
# Retorna representação técnica.
# ==============================================================

print(repr("Olá"))
# endregion


# region | reversed()
# ==============================================================
# reversed()
# Retorna um iterador que percorre o objeto em ordem reversa.
# ==============================================================

print(list(reversed([1, 2, 3])))
# endregion


# region | round()
# ==============================================================
# round()
# Arredonda números.
# ==============================================================

print(round(3.14159, 2))
# endregion


# region | set()
# ==============================================================
# set()
# Cria conjunto.
# ==============================================================

print(set([1, 1, 2]))
# endregion


# region | setattr()
# ==============================================================
# setattr()
# Define atributo dinamicamente.
# ==============================================================

class Pessoa:
    pass

setattr(Pessoa, "nome", "Carlos")
# endregion


# region | slice()
# ==============================================================
# slice()
# Cria objeto de fatiamento.
# ==============================================================

print(slice(0, 5))
# endregion


# region | sorted()
# ==============================================================
# sorted()
# Percorre um iterável e retorna uma NOVA lista ordenada, sem modificar o objeto original.
# ==============================================================

print(sorted([3, 1, 2]))
# endregion


# region | staticmethod()
# ==============================================================
# staticmethod()
# Define método estático.
# ==============================================================

class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b
# endregion


# region | str()
# ==============================================================
# str()
# Converte para texto.
# ==============================================================

print(str(100))
# endregion


# region | sum()
# ==============================================================
# sum()
# Soma elementos.
# ==============================================================

print(sum([1, 2, 3]))
# endregion


# region | super()
# ==============================================================
# super()
# Acessa comportamento da superclasse.
# ==============================================================

class Animal:
    def falar(self):
        print("Som")

class Cachorro(Animal):
    def falar(self):
        super().falar()
        print("Au au")
# endregion


# region | tuple()
# ==============================================================
# tuple()
# Cria tupla.
# ==============================================================

print(tuple([1, 2, 3]))
# endregion


# region | type()
# ==============================================================
# type()
# Retorna tipo do objeto.
# ==============================================================

print(type(10))
# endregion


# region | vars()
# ==============================================================
# vars()
# Retorna atributos internos.
# ==============================================================

print(vars())
# endregion


# region | zip()
# ==============================================================
# zip()
# Retorna um iterador de tuplas que combina, posição a posição, elementos de iteráveis.
# ==============================================================

print(list(zip([1, 2], ["a", "b"])))
# endregion


# region | __import__()
# ==============================================================
# __import__()
# Importa módulos dinamicamente.
# ==============================================================

modulo = __import__("math")
# endregion

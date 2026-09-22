# ==========================================================
# COLLECTION METHODS REFERENCE
# ==========================================================
#
# Este comentário serve como placeholder de um índice dos métodos nativos das
# principais estruturas de dados do Python.
#
# Objetivo:
# - Saber quais métodos existem.
# - Saber em qual estrutura eles estão disponíveis.
# - Estudar posteriormente seu funcionamento.
#
# ==========================================================

# ==========================================================
# MÉTODOS DAS ESTRUTURAS DE DADOS / COLEÇÕES
# ==========================================================

# region | Legenda

    # region | Método

        # um método é uma função associada a um objeto ou à classe desse objeto.
        #
        # sintaxe geral:
        #
        # objeto.metodo(argumentos)
        #
        # o objeto antes do ponto determina sobre qual objeto
        # o método será executado.

    # endregion

    # region | Métodos Que Modificam O Próprio Objeto

        # alguns métodos alteram diretamente o objeto sobre o qual
        # são chamados.
        #
        # exemplo conceitual:
        #
        # lista.append(4)
        #
        # nesse caso, a própria lista é modificada.

    # endregion

    # region | Métodos Que Retornam Um Novo Objeto

        # estruturas imutáveis, como strings, não podem ser alteradas
        # depois de criadas.
        #
        # por isso, métodos dessas estruturas normalmente retornam
        # um novo objeto contendo o resultado da operação.
        #
        # exemplo:
        #
        # texto = "PYTHON"
        # novo_texto = texto.lower()
        #
        # texto:
        # -> "PYTHON"
        #
        # novo_texto:
        # -> "python"

    # endregion

    # region | Retorno None

        # vários métodos que modificam diretamente uma estrutura mutável
        # retornam None.
        #
        # isso ocorre porque o objetivo do método é produzir um efeito
        # sobre o próprio objeto e não fabricar um novo objeto como resultado.

    # endregion

# endregion

# region | List

    # region | append()

        # adiciona um único objeto ao final da lista.
        #
        # exemplo:
        #
        # lista = [1, 2]
        # lista.append(3)
        #
        # resultado da lista:
        # -> [1, 2, 3]
        #
        # o objeto fornecido é inserido como um único elemento.
        #
        # exemplo:
        #
        # lista = [1, 2]
        # lista.append([3, 4])
        #
        # resultado:
        # -> [1, 2, [3, 4]]
        #
        # modifica a própria lista.
        # retorna:
        # -> None

    # endregion

    # region | extend()

        # adiciona à lista os elementos provenientes de um iterável.
        #
        # diferente de append(), não adiciona o iterável como
        # um único elemento: percorre seus elementos e os adiciona.
        #
        # exemplo:
        #
        # lista = [1, 2]
        # lista.extend([3, 4])
        #
        # resultado:
        # -> [1, 2, 3, 4]
        #
        # modifica a própria lista.
        # retorna:
        # -> None

    # endregion

    # region | insert()

        # insere um objeto em uma posição específica da lista.
        #
        # sintaxe:
        #
        # lista.insert(indice, objeto)
        #
        # exemplo:
        #
        # lista = [1, 3]
        # lista.insert(1, 2)
        #
        # resultado:
        # -> [1, 2, 3]
        #
        # modifica a própria lista.
        # retorna:
        # -> None

    # endregion

    # region | remove()

        # remove a primeira ocorrência de determinado valor da lista.
        #
        # exemplo:
        #
        # lista = [1, 2, 2, 3]
        # lista.remove(2)
        #
        # resultado:
        # -> [1, 2, 3]
        #
        # a remoção ocorre pelo valor, não pelo índice.
        #
        # se o valor não existir:
        # -> ValueError
        #
        # modifica a própria lista.
        # retorna:
        # -> None

    # endregion

    # region | pop()

        # remove um elemento da lista e retorna o objeto removido.
        #
        # sem argumento:
        #
        # lista.pop()
        #
        # remove o último elemento.
        #
        # com índice:
        #
        # lista.pop(indice)
        #
        # remove o elemento existente naquela posição.
        #
        # exemplo:
        #
        # lista = [10, 20, 30]
        # valor = lista.pop(1)
        #
        # lista:
        # -> [10, 30]
        #
        # valor:
        # -> 20
        #
        # modifica a própria lista.
        # retorna:
        # -> objeto removido

    # endregion

    # region | clear()

        # remove todos os elementos da lista.
        #
        # exemplo:
        #
        # lista = [1, 2, 3]
        # lista.clear()
        #
        # resultado:
        # -> []
        #
        # modifica a própria lista.
        # retorna:
        # -> None

    # endregion

    # region | copy()

        # cria uma cópia rasa da lista.
        #
        # exemplo:
        #
        # lista = [1, 2, 3]
        # copia = lista.copy()
        #
        # lista e copia são listas diferentes,
        # embora inicialmente possuam referências equivalentes
        # para os elementos internos.
        #
        # retorna:
        # -> nova list

    # endregion

    # region | count()

        # conta quantas vezes determinado valor aparece na lista.
        #
        # exemplo:
        #
        # lista = [1, 2, 2, 2, 3]
        # lista.count(2)
        #
        # -> 3
        #
        # não modifica a lista.
        # retorna:
        # -> int

    # endregion

    # region | index()

        # procura determinado valor e retorna o índice
        # de sua primeira ocorrência.
        #
        # exemplo:
        #
        # lista = ["a", "b", "c"]
        # lista.index("b")
        #
        # -> 1
        #
        # se o valor não existir:
        # -> ValueError
        #
        # não modifica a lista.
        # retorna:
        # -> int

    # endregion

    # region | reverse()

        # inverte a ordem dos elementos da própria lista.
        #
        # exemplo:
        #
        # lista = [1, 2, 3]
        # lista.reverse()
        #
        # resultado:
        # -> [3, 2, 1]
        #
        # modifica a própria lista.
        # retorna:
        # -> None

    # endregion

    # region | sort()

        # ordena os elementos da própria lista.
        #
        # exemplo:
        #
        # lista = [3, 1, 2]
        # lista.sort()
        #
        # resultado:
        # -> [1, 2, 3]
        #
        # ordem reversa:
        #
        # lista.sort(reverse=True)
        #
        # resultado:
        # -> [3, 2, 1]
        #
        # também pode receber uma função através do parâmetro key
        # para determinar qual informação será utilizada na ordenação.
        #
        # modifica a própria lista.
        # retorna:
        # -> None

    # endregion

# endregion

# region | Tuple

    # region | count()

        # conta quantas vezes determinado valor aparece na tupla.
        #
        # exemplo:
        #
        # tupla = (1, 2, 2, 3)
        # tupla.count(2)
        #
        # -> 2
        #
        # não modifica a tupla.
        # retorna:
        # -> int

    # endregion

    # region | index()

        # procura determinado valor e retorna o índice
        # de sua primeira ocorrência.
        #
        # exemplo:
        #
        # tupla = ("a", "b", "c")
        # tupla.index("b")
        #
        # -> 1
        #
        # se o valor não existir:
        # -> ValueError
        #
        # não modifica a tupla.
        # retorna:
        # -> int

    # endregion

# endregion

# region | Dictionary

    # region | get()

        # acessa o valor associado a determinada chave.
        #
        # exemplo:
        #
        # dados = {"nome": "Victor"}
        # dados.get("nome")
        #
        # -> "Victor"
        #
        # diferença importante em relação a:
        #
        # dados["idade"]
        #
        # se a chave não existir, [] gera:
        # -> KeyError
        #
        # get() retorna por padrão:
        # -> None
        #
        # também é possível definir um valor alternativo:
        #
        # dados.get("idade", 0)
        #
        # -> 0
        #
        # não modifica o dicionário.

    # endregion

    # region | keys()

        # retorna uma visão dinâmica contendo as chaves
        # existentes no dicionário.
        #
        # exemplo:
        #
        # dados = {"nome": "Victor", "idade": 21}
        # dados.keys()
        #
        # representação:
        # -> dict_keys(["nome", "idade"])
        #
        # não retorna uma list diretamente.
        # retorna:
        # -> dict_keys

    # endregion

    # region | values()

        # retorna uma visão dinâmica contendo os valores
        # existentes no dicionário.
        #
        # exemplo:
        #
        # dados = {"nome": "Victor", "idade": 21}
        # dados.values()
        #
        # representação:
        # -> dict_values(["Victor", 21])
        #
        # retorna:
        # -> dict_values

    # endregion

    # region | items()

        # retorna uma visão dinâmica contendo os pares
        # chave e valor do dicionário.
        #
        # cada associação é apresentada como uma tupla:
        #
        # (chave, valor)
        #
        # exemplo:
        #
        # dados = {"nome": "Victor", "idade": 21}
        # dados.items()
        #
        # representação:
        # -> dict_items([("nome", "Victor"), ("idade", 21)])
        #
        # muito utilizado em loops:
        #
        # for chave, valor in dados.items():
        #     ...
        #
        # retorna:
        # -> dict_items

    # endregion

    # region | update()

        # adiciona novas associações ao dicionário
        # ou atualiza valores de chaves já existentes.
        #
        # exemplo:
        #
        # dados = {"nome": "Victor"}
        #
        # dados.update({"idade": 21})
        #
        # resultado:
        # -> {"nome": "Victor", "idade": 21}
        #
        # caso uma chave já exista:
        #
        # dados.update({"nome": "Carlos"})
        #
        # o valor associado à chave é substituído.
        #
        # modifica o próprio dicionário.
        # retorna:
        # -> None

    # endregion

    # region | pop()

        # remove determinada chave e retorna o valor
        # que estava associado a ela.
        #
        # exemplo:
        #
        # dados = {"nome": "Victor", "idade": 21}
        # idade = dados.pop("idade")
        #
        # dados:
        # -> {"nome": "Victor"}
        #
        # idade:
        # -> 21
        #
        # modifica o próprio dicionário.
        # retorna:
        # -> valor removido

    # endregion

    # region | popitem()

        # remove e retorna a última associação inserida
        # no dicionário.
        #
        # retorna uma tupla:
        #
        # (chave, valor)
        #
        # exemplo:
        #
        # dados = {"nome": "Victor", "idade": 21}
        # dados.popitem()
        #
        # -> ("idade", 21)
        #
        # modifica o próprio dicionário.

    # endregion

    # region | clear()

        # remove todas as associações do dicionário.
        #
        # exemplo:
        #
        # dados = {"nome": "Victor", "idade": 21}
        # dados.clear()
        #
        # resultado:
        # -> {}
        #
        # modifica o próprio dicionário.
        # retorna:
        # -> None

    # endregion

    # region | copy()

        # cria uma cópia rasa do dicionário.
        #
        # exemplo:
        #
        # dados = {"nome": "Victor"}
        # copia = dados.copy()
        #
        # retorna:
        # -> novo dict

    # endregion

    # region | setdefault()

        # procura determinada chave no dicionário.
        #
        # se a chave já existir:
        # -> retorna o valor associado.
        #
        # se a chave não existir:
        # -> cria a chave utilizando um valor padrão;
        # -> retorna esse valor.
        #
        # exemplo:
        #
        # dados = {}
        #
        # dados.setdefault("idade", 21)
        #
        # resultado:
        # -> {"idade": 21}
        #
        # retorno:
        # -> 21
        #
        # caso nenhum valor padrão seja informado:
        # -> None

    # endregion

# endregion

# region | Set

    # region | add()

        # adiciona um único elemento ao conjunto.
        #
        # exemplo:
        #
        # conjunto = {1, 2}
        # conjunto.add(3)
        #
        # resultado:
        # -> {1, 2, 3}
        #
        # se o elemento já existir, o conjunto permanece
        # sem uma duplicação desse elemento.
        #
        # modifica o próprio set.
        # retorna:
        # -> None

    # endregion

    # region | update()

        # adiciona ao conjunto os elementos provenientes
        # de um ou mais iteráveis.
        #
        # exemplo:
        #
        # conjunto = {1, 2}
        # conjunto.update([2, 3, 4])
        #
        # resultado:
        # -> {1, 2, 3, 4}
        #
        # modifica o próprio set.
        # retorna:
        # -> None

    # endregion

    # region | remove()

        # remove determinado elemento do conjunto.
        #
        # se o elemento não existir:
        # -> KeyError
        #
        # modifica o próprio set.
        # retorna:
        # -> None

    # endregion

    # region | discard()

        # remove determinado elemento do conjunto.
        #
        # diferente de remove(), se o elemento não existir,
        # nenhum erro é gerado.
        #
        # modifica o próprio set.
        # retorna:
        # -> None

    # endregion

    # region | pop()

        # remove e retorna um elemento do conjunto.
        #
        # como sets não possuem uma ordem de posição utilizável
        # como listas, não se deve depender de qual elemento
        # será removido.
        #
        # modifica o próprio set.
        # retorna:
        # -> elemento removido

    # endregion

    # region | clear()

        # remove todos os elementos do conjunto.
        #
        # resultado:
        # -> set vazio
        #
        # modifica o próprio set.
        # retorna:
        # -> None

    # endregion

    # region | copy()

        # cria uma cópia rasa do conjunto.
        #
        # retorna:
        # -> novo set

    # endregion

    # region | union()

        # cria um novo conjunto contendo todos os elementos
        # presentes nos conjuntos envolvidos.
        #
        # exemplo:
        #
        # a = {1, 2}
        # b = {2, 3}
        #
        # a.union(b)
        #
        # -> {1, 2, 3}
        #
        # não modifica os conjuntos originais.
        # retorna:
        # -> novo set

    # endregion

    # region | intersection()

        # cria um novo conjunto contendo apenas os elementos
        # presentes em ambos os conjuntos.
        #
        # exemplo:
        #
        # a = {1, 2}
        # b = {2, 3}
        #
        # a.intersection(b)
        #
        # -> {2}
        #
        # retorna:
        # -> novo set

    # endregion

    # region | difference()

        # cria um novo conjunto contendo os elementos
        # existentes no primeiro conjunto e ausentes no segundo.
        #
        # exemplo:
        #
        # a = {1, 2, 3}
        # b = {2, 3, 4}
        #
        # a.difference(b)
        #
        # -> {1}
        #
        # a ordem dos conjuntos importa.
        #
        # retorna:
        # -> novo set

    # endregion

    # region | symmetric_difference()

        # cria um novo conjunto contendo os elementos
        # que pertencem a apenas um dos conjuntos.
        #
        # os elementos existentes em ambos são excluídos.
        #
        # exemplo:
        #
        # a = {1, 2, 3}
        # b = {2, 3, 4}
        #
        # a.symmetric_difference(b)
        #
        # -> {1, 4}
        #
        # retorna:
        # -> novo set

    # endregion

# endregion

# region | Frozenset

    # region | Característica Geral

        # frozenset é imutável.
        #
        # portanto, não possui métodos destinados a adicionar
        # ou remover elementos diretamente do próprio objeto.
        #
        # suas operações produzem novos conjuntos como resultado.

    # endregion

    # region | union()

        # retorna um novo conjunto contendo os elementos
        # presentes nas estruturas envolvidas.

    # endregion

    # region | intersection()

        # retorna um novo conjunto contendo apenas os elementos
        # presentes em ambas as estruturas.

    # endregion

    # region | difference()

        # retorna um novo conjunto contendo os elementos
        # presentes no primeiro e ausentes no segundo.

    # endregion

    # region | symmetric_difference()

        # retorna um novo conjunto contendo os elementos
        # que pertencem a apenas uma das estruturas.

    # endregion

    # region | issubset()

        # verifica se todos os elementos do objeto estão
        # contidos em outro conjunto.
        #
        # exemplo conceitual:
        #
        # a = frozenset({1, 2})
        # b = {1, 2, 3}
        #
        # a.issubset(b)
        #
        # -> True
        #
        # retorna:
        # -> bool

    # endregion

    # region | issuperset()

        # verifica se o objeto contém todos os elementos
        # existentes no conjunto fornecido.
        #
        # retorna:
        # -> bool

    # endregion

    # region | isdisjoint()

        # verifica se duas estruturas não possuem
        # nenhum elemento em comum.
        #
        # se não houver elementos compartilhados:
        # -> True
        #
        # retorna:
        # -> bool

    # endregion

# endregion

# region | String

    # region | OBS

        # strings são imutáveis.
        #
        # portanto, os métodos abaixo não alteram
        # a string original.
        #
        # quando há transformação textual,
        # um novo objeto str é retornado.

    # endregion

    # region | lower()

        # retorna uma nova string com os caracteres
        # convertidos para minúsculos quando aplicável.
        #
        # exemplo:
        #
        # "Python".lower()
        #
        # -> "python"
        #
        # a string original permanece inalterada.

    # endregion

    # region | upper()

        # retorna uma nova string com os caracteres
        # convertidos para maiúsculos quando aplicável.
        #
        # exemplo:
        #
        # "Python".upper()
        #
        # -> "PYTHON"

    # endregion

    # region | capitalize()

        # retorna uma string com o primeiro caractere
        # convertido para maiúsculo e os demais para minúsculos.
        #
        # exemplo:
        #
        # "pYTHON".capitalize()
        #
        # -> "Python"

    # endregion

    # region | title()

        # retorna uma string em que o início das palavras
        # é convertido para maiúsculo segundo as regras
        # utilizadas pelo método.
        #
        # exemplo:
        #
        # "linguagem python".title()
        #
        # -> "Linguagem Python"

    # endregion

    # region | strip()

        # remove caracteres das extremidades da string.
        #
        # sem argumento, remove principalmente
        # espaços e outros caracteres de whitespace.
        #
        # exemplo:
        #
        # "  Python  ".strip()
        #
        # -> "Python"
        #
        # também pode receber caracteres específicos
        # que serão removidos das extremidades.

    # endregion

    # region | replace()

        # retorna uma nova string substituindo ocorrências
        # de determinado trecho por outro.
        #
        # sintaxe:
        #
        # texto.replace(antigo, novo)
        #
        # exemplo:
        #
        # "Python é legal".replace("legal", "ótimo")
        #
        # -> "Python é ótimo"

    # endregion

    # region | split()

        # divide uma string em partes e retorna uma lista.
        #
        # exemplo:
        #
        # "Python Java C".split()
        #
        # -> ["Python", "Java", "C"]
        #
        # é possível especificar um separador:
        #
        # "a,b,c".split(",")
        #
        # -> ["a", "b", "c"]
        #
        # retorna:
        # -> list

    # endregion

    # region | join()

        # une elementos de um iterável de strings utilizando
        # a string que chamou o método como separador.
        #
        # exemplo:
        #
        # nomes = ["Python", "Java", "C"]
        #
        # ", ".join(nomes)
        #
        # -> "Python, Java, C"
        #
        # uma forma útil de leitura:
        #
        # separador.join(iteravel_de_strings)

    # endregion

    # region | find()

        # procura uma substring dentro da string
        # e retorna o índice da primeira ocorrência.
        #
        # exemplo:
        #
        # "Python".find("t")
        #
        # -> 2
        #
        # se o trecho não for encontrado:
        # -> -1
        #
        # isso diferencia find() de index(),
        # que gera ValueError quando não encontra.

    # endregion

    # region | startswith()

        # verifica se a string começa com determinado
        # prefixo.
        #
        # exemplo:
        #
        # "Python".startswith("Py")
        #
        # -> True
        #
        # retorna:
        # -> bool

    # endregion

    # region | endswith()

        # verifica se a string termina com determinado
        # sufixo.
        #
        # exemplo:
        #
        # "arquivo.py".endswith(".py")
        #
        # -> True
        #
        # retorna:
        # -> bool

    # endregion

# endregion

# region | Bytes

    # region | Característica Geral

        # bytes representa uma sequência imutável de valores
        # inteiros no intervalo de 0 a 255.
        #
        # vários métodos possuem comportamento semelhante
        # aos métodos de strings, mas operam sobre bytes.

    # endregion

    # region | decode()

        # converte uma sequência de bytes em str
        # utilizando determinada codificação.
        #
        # exemplo:
        #
        # dados = b"Python"
        # dados.decode("utf-8")
        #
        # -> "Python"
        #
        # retorna:
        # -> str

    # endregion

    # region | find()

        # procura uma subsequência de bytes e retorna
        # o índice de sua primeira ocorrência.
        #
        # se não encontrar:
        # -> -1

    # endregion

    # region | split()

        # divide a sequência de bytes utilizando
        # determinado separador.
        #
        # retorna:
        # -> list de objetos bytes

    # endregion

    # region | join()

        # une objetos bytes provenientes de um iterável
        # utilizando o objeto que chamou join()
        # como separador.
        #
        # retorna:
        # -> novo objeto bytes

    # endregion

    # region | startswith()

        # verifica se a sequência começa com
        # determinada subsequência de bytes.
        #
        # retorna:
        # -> bool

    # endregion

    # region | endswith()

        # verifica se a sequência termina com
        # determinada subsequência de bytes.
        #
        # retorna:
        # -> bool

    # endregion

# endregion

# region | Bytearray

    # region | Característica Geral

        # bytearray possui comportamento semelhante a bytes,
        # mas é uma estrutura mutável.
        #
        # por isso, possui métodos capazes de modificar
        # diretamente sua sequência de bytes.

    # endregion

    # region | append()

        # adiciona um único valor inteiro entre 0 e 255
        # ao final do bytearray.
        #
        # modifica o próprio objeto.
        # retorna:
        # -> None

    # endregion

    # region | extend()

        # adiciona vários bytes provenientes de um iterável
        # ao final do bytearray.
        #
        # modifica o próprio objeto.
        # retorna:
        # -> None

    # endregion

    # region | insert()

        # insere um valor de byte em determinada posição.
        #
        # sintaxe:
        #
        # objeto.insert(indice, valor)
        #
        # modifica o próprio objeto.
        # retorna:
        # -> None

    # endregion

    # region | pop()

        # remove e retorna o valor existente
        # em determinada posição.
        #
        # sem índice, remove o último elemento.
        #
        # modifica o próprio objeto.
        # retorna:
        # -> int

    # endregion

    # region | remove()

        # remove a primeira ocorrência de determinado
        # valor do bytearray.
        #
        # modifica o próprio objeto.
        # retorna:
        # -> None

    # endregion

    # region | clear()

        # remove todos os elementos do bytearray.
        #
        # modifica o próprio objeto.
        # retorna:
        # -> None

    # endregion

# endregion
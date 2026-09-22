# ==========================================================
# SINTAXE DAS ESTRUTURAS DE DADOS / COLEÇÕES
# ==========================================================

# Este arquivo trata da sintaxe utilizada para criar, acessar,
# alterar e operar estruturalmente sobre as principais coleções
# nativas do Python.
#
# Métodos específicos de cada estrutura são tratados separadamente
# em Data_structures_methods.py.

# ==========================================================


# region | Conceitos gerais

    # region | Literal

        # Um literal é uma representação escrita diretamente no código
        # que permite ao Python construir um objeto daquele tipo.

        # Exemplos:

        # lista = [1, 2, 3]
        # tupla = (1, 2, 3)
        # dicionario = {"nome": "Victor", "idade": 21}
        # conjunto = {1, 2, 3}
        # texto = "Python"

    # endregion

    # region | Acesso

        # Algumas coleções permitem acessar individualmente elementos
        # através da sintaxe:

        # objeto[identificador]

        # O significado do identificador depende da estrutura.

        # Em sequências:
            # objeto[indice] -> retorna o elemento naquela posição.

        # Em dicionários:
            # objeto[chave] -> retorna o valor associado àquela chave.

    # endregion

    # region | Atribuição através de []

        # Em estruturas mutáveis que permitem atribuição individual,
        # [] também pode aparecer como ALVO de uma atribuição.

        # estrutura[identificador] = valor

        # Nesse contexto, [] não está simplesmente lendo um valor:
        # está indicando o local/associação que receberá a atribuição.

    # endregion


# endregion

# region | Listas

    # region | Criação

        # lista = [10, 20, 30]

        # [] representa um literal de lista.

        # lista_vazia = []

    # endregion

    # region | Acesso por índice

        # lista = [10, 20, 30]

        # lista[0]  -> 10
        # lista[1]  -> 20
        # lista[2]  -> 30

        # lista[indice] retorna o objeto armazenado naquela posição.

    # endregion

    # region | Índices negativos

        # lista = [10, 20, 30]

        # lista[-1]  -> 30
        # lista[-2]  -> 20

        # Índices negativos percorrem a sequência a partir do final.

    # endregion

    # region | Atribuição por índice

        # lista = [10, 20, 30]

        # lista[1] = 50

        # Resultado:
        # [10, 50, 30]

        # Como list é mutável, uma posição existente pode receber
        # uma nova referência durante a execução.

    # endregion

    # region | Slicing

        # lista = [10, 20, 30, 40, 50]

        # lista[1:4]

        # -> [20, 30, 40]

        # Sintaxe geral:

        # sequencia[inicio:fim:passo]

        # inicio -> posição inicial incluída.
        # fim    -> posição final não incluída.
        # passo  -> distância entre os elementos selecionados.

    # endregion

    # region | Pertencimento

        # lista = [10, 20, 30]

        # 20 in lista
        # -> True

        # O operador "in" verifica se determinado elemento
        # existe dentro da coleção.

    # endregion

# endregion

# region | Tuplas

    # region | Criação

        # tupla = (10, 20, 30)

        # () é a representação literal comum de uma tupla.

    # endregion

    # region | Tupla de um único elemento

        # tupla = (10,)

        # A vírgula é o elemento sintático que efetivamente
        # caracteriza uma tupla de um único elemento.

        # nao_e_tupla = (10)

        # -> int

    # endregion

    # region | Acesso

        # tupla = (10, 20, 30)

        # tupla[0]
        # -> 10

        # Tuplas são indexadas como listas.

    # endregion

    # region | Imutabilidade

        # tupla = (10, 20, 30)

        # tupla[0] = 50
        # -> TypeError

        # A sintaxe de acesso é válida,
        # mas a atribuição em uma posição não é,
        # pois tuple é imutável.

    # endregion

    # region | Slicing

        # tupla = (10, 20, 30, 40)

        # tupla[1:3]

        # -> (20, 30)

        # O slicing cria uma nova tupla contendo
        # os elementos selecionados.

    # endregion

# endregion

# region | Dicionários

    # region | Criação

        # dicionario = {
        #     "nome": "Victor",
        #     "idade": 21
        # }

        # Estrutura:

        # chave : valor

        # Cada entrada representa uma associação
        # entre uma chave e um valor.

    # endregion

    # region | Dicionário vazio

        # dicionario = {}

        # IMPORTANTE:
        # {} sozinho cria um dicionário vazio,
        # não um set vazio.

    # endregion

    # region | Acesso através de chave

        # dicionario = {
        #     "nome": "Victor",
        #     "idade": 21
        # }

        # dicionario["nome"]

        # -> "Victor"

        # Dentro de [] colocamos a CHAVE utilizada para realizar a busca.

        # A expressão inteira:

        # dicionario[chave]

        # retorna o VALOR associado àquela chave.

        # Portanto:

        # chave:
            # "nome"

        # expressão:
            # dicionario["nome"]

        # resultado:
            # "Victor"

    # endregion

    # region | Atribuição através de chave

        # dicionario = {}

        # dicionario["nome"] = "Victor"

        # Resultado:

        # {"nome": "Victor"}

        # Quando dicionario[chave] aparece no lado esquerdo
        # de uma atribuição, ele funciona como ALVO da atribuição.

        # Se a chave NÃO existir:
            # uma nova associação chave -> valor é criada.

        # Se a chave JÁ existir:
            # o valor associado a ela é substituído.

    # endregion

    # region | Criação de uma nova associação

        # dados = {}

        # dados["idade"] = 21

        # Como "idade" ainda não existia:

        # {} -> {"idade": 21}

        # A própria atribuição é suficiente para criar
        # a nova associação dentro do dicionário.

    # endregion

    # region | Atualização de uma associação existente

        # dados = {
        #     "idade": 20
        # }

        # dados["idade"] = 21

        # Resultado:

        # {"idade": 21}

        # A chave não é duplicada.
        # O valor anteriormente associado é substituído.

    # endregion

    # region | Atribuição composta em valores

        # quantidade_por_genero = {
        #     "Ficção": 3
        # }

        # quantidade_por_genero["Ficção"] += 4

        # Resultado:

        # {"Ficção": 7}

        # A atribuição composta:

        # dicionario[chave] += valor

        # pode ser interpretada conceitualmente como:

        # dicionario[chave] =
        #     dicionario[chave] + valor

        # Portanto ocorre:

            # 1. a chave é utilizada para acessar o valor existente;
            # 2. uma operação é realizada com esse valor;
            # 3. o resultado é atribuído novamente à mesma chave.

        # Nesse caso, a chave precisa possuir um valor previamente
        # associado para que ele possa ser lido.

    # endregion

    # region | Diferença entre = e += no acesso por chave

        # ATRIBUIÇÃO:

        # dicionario[chave] = valor

        # -> cria a associação caso a chave não exista;
        # -> substitui o valor caso a chave já exista.


        # ATRIBUIÇÃO COMPOSTA:

        # dicionario[chave] += valor

        # -> primeiro acessa o valor já associado à chave;
        # -> soma o novo valor;
        # -> armazena o resultado novamente naquela chave.

    # endregion

    # region | Operador in

        # dicionario = {
        #     "Ficção": 7,
        #     "Romance": 2
        # }

        # "Ficção" in dicionario
        # -> True

        # Quando "in" é utilizado diretamente sobre um dicionário,
        # a busca ocorre nas CHAVES, não nos valores.

        # Portanto:

        # if "Ficção" in dicionario:
        #     pass

        # pergunta conceitualmente:

        # "Existe uma chave chamada 'Ficção'
        # neste dicionário?"

    # endregion

    # region | Caso prático - acumulação de valores

        # quantidade_por_genero = {}

        # for livro in livros:

        #     if livro.genero in quantidade_por_genero:

        #         quantidade_por_genero[livro.genero] += livro.quantidade

                # A chave já existe:
                # utiliza-a para acessar o valor associado;
                # soma livro.quantidade;
                # grava o novo resultado.

            # else:

            #     quantidade_por_genero[livro.genero] = livro.quantidade

                # A chave ainda não existe:
                # cria uma nova associação:
                #
                # livro.genero -> livro.quantidade


        # Exemplo de progressão:

        # {}
        #
        # primeiro livro:
        # gênero = "Ficção"
        # quantidade = 3
        #
        # {"Ficção": 3}
        #
        # segundo livro:
        # gênero = "Ficção"
        # quantidade = 4
        #
        # {"Ficção": 7}

    # endregion

    # region | Chaves são únicas

        # Um dicionário não possui duas entradas independentes
        # com a mesma chave.

        # dicionario = {
        #     "nome": "Victor"
        # }

        # dicionario["nome"] = "Carlos"

        # Resultado:

        # {"nome": "Carlos"}

        # A associação anterior é atualizada.

    # endregion

# endregion

# region | Sets / Conjuntos

    # region | Criação

        # conjunto = {1, 2, 3}

        # Valores separados por vírgulas dentro de {}
        # sem associações chave:valor formam um set.

    # endregion

    # region | Set vazio

        # conjunto = set()

        # {} NÃO cria um set vazio.

        # dicionario = {}
        # -> dict

        # conjunto = set()
        # -> set

    # endregion

    # region | Unicidade

        # conjunto = {1, 2, 2, 3, 3}

        # Resultado lógico:

        # {1, 2, 3}

        # Sets não mantêm elementos duplicados.

    # endregion

    # region | Ausência de acesso por índice

        # conjunto = {10, 20, 30}

        # conjunto[0]
        # -> TypeError

        # Sets não são sequências indexadas.

    # endregion

    # region | Pertencimento

        # conjunto = {10, 20, 30}

        # 20 in conjunto

        # -> True

        # A verificação de pertencimento é uma das operações
        # centrais de um set.

    # endregion


# endregion

# region | Strings

    # region | Criação

        # texto = "Python"

        # Strings representam sequências imutáveis
        # de caracteres Unicode.

    # endregion

    # region | Acesso por índice

        # texto = "Python"

        # texto[0]
        # -> "P"

        # texto[-1]
        # -> "n"

    # endregion

    # region | Slicing

        # texto = "Python"

        # texto[0:3]

        # -> "Pyt"

        # Assim como outras sequências,
        # strings suportam slicing.

    # endregion

    # region | Imutabilidade

        # texto = "Python"

        # texto[0] = "J"
        # -> TypeError

        # É possível acessar individualmente os caracteres,
        # mas não substituir uma posição da string existente.

    # endregion

    # region | Pertencimento

        # "Py" in "Python"
        # -> True

        # "Java" in "Python"
        # -> False

    # endregion


# endregion

# region | Estruturas aninhadas

    # Coleções podem armazenar referências para outros objetos,
    # incluindo outras coleções e instâncias de classes.

    # region | Lista contendo objetos

        # livro1 = Livro("1984", "George Orwell", "Ficção", 3)

        # livros = [livro1]

        # A lista possui um elemento:
        # uma referência para o objeto livro1.

        # O objeto referenciado, por sua vez, possui
        # diversos atributos internos.

        # livros[0].titulo

        # Ordem conceitual:

        # livros
        # -> [0]
        # -> objeto Livro
        # -> .titulo
        # -> "1984"

    # endregion

    # region | Lista contendo dicionários

        # pessoas = [
        #     {"nome": "Victor", "idade": 21},
        #     {"nome": "Carlos", "idade": 25}
        # ]

        # pessoas[0]["nome"]

        # -> "Victor"

        # Ordem:

        # pessoas[0]
            # retorna o primeiro dicionário.

        # ["nome"]
            # usa a chave "nome" nesse dicionário
            # e retorna seu valor.

    # endregion

    # region | Dicionário contendo listas

        # dados = {
        #     "notas": [8, 9, 7]
        # }

        # dados["notas"][0]

        # -> 8

        # dados["notas"]
            # -> retorna a lista [8, 9, 7]

        # [0]
            # -> acessa o primeiro elemento dessa lista.

    # endregion

# endregion
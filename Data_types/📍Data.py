
# region | Dados

    # informações ou valores representados em um programa.
    # em Python, os dados são representados por objetos ou
    # por relações entre objetos.

    # region | Objetos

        # entidades que representam dados em Python.
        # todo objeto possui valor, tipo e identidade.

        # region | Valor


            # conteúdo ou estado representado pelo objeto.


        # endregion
        # region | Tipo


            # determina os valores que um objeto pode representar
            # e as operações que ele suporta.
            # permanece constante durante a existência do objeto.


            # region | Classe


                # mecanismo utilizado para definir tipos em Python.
                # os próprios tipos também são objetos.


            # endregion
            # region | Instância


                # objeto pertencente a uma classe.
                # por exemplo, [1, 2] é uma instância de list.


            # endregion
            # region | Mutabilidade


                # possibilidade de modificar o estado de um objeto.
                # é determinada pelo tipo: list é mutável;
                # int é imutável.


            # endregion

        # endregion
        # region | Identidade


            # propriedade que individualiza um objeto durante
            # sua existência, independentemente do tipo ou valor.
            # permite distinguir objetos diferentes e reconhecer
            # referências que apontam para o mesmo objeto.
            # pode ser consultada com id() e comparada com is.


            # region | Curiosidade — CPython


                # a identidade corresponde ao endereço do objeto
                # na memória virtual do processo.
                # id() retorna esse endereço como um inteiro.
                # esse não é o endereço físico na RAM.

                # o endereço permanece associado ao objeto
                # durante sua existência, mas pode ser reutilizado
                # após sua destruição.

                # essa representação é específica do CPython;
                # outras implementações podem utilizar outra forma.


            # endregion

        # endregion

    # endregion
    # region | Variáveis

        # nomes associados a objetos dentro de um escopo.
        # permitem referenciar e reutilizar objetos e resultados
        # posteriormente, enquanto estiverem acessíveis.

        # region | Escopo


            # contexto em que um nome pode ser reconhecido
            # e acessado durante a execução do programa.
            # Python possui escopos locais, envolventes,
            # globais e embutidos (built-in).


        # endregion

    # endregion
    # region | Tipagem do Python

        # características do sistema de tipos da linguagem.

        # region | Dinâmica

            # os objetos possuem tipos, enquanto os nomes
            # podem ser associados a objetos de tipos diferentes
            # durante a execução.

        # endregion
        # region | Forte

            # tipos incompatíveis não são convertidos
            # arbitrariamente para permitir operações.
            # algumas conversões implícitas são previstas
            # pela própria linguagem.

        # endregion

    # endregion
    # region | literais

        # um literal é uma notação escrita diretamente no código-fonte que representa um valor. Quando o literal é avaliado, o Python fornece um objeto correspondente. exemplo:
            
        # 21        -> literal inteiro.
        # 3.14      -> literal de ponto flutuante.
        # "Python"  -> string literal.
        # True      -> constante booleana.

    # endregion    

    # OBS:
        # todos os dados em Python são representados por objetos.
        # termos como "primitivo" são classificações didáticas,
        # não uma categoria de valores sem objetos.

        # RAM é memória volátil, não persistência.
        # persistência normalmente envolve SSD, HD ou outros
        # meios de armazenamento não volátil.


# endregion

#============================================================
# Extra: 
    # Uma coleção é uma abstração criada pela linguagem.
    # Em memória, tudo é representado como bytes.
    # Cabe à linguagem interpretar esses bytes como um único
    # valor ou como uma estrutura contendo múltiplos valores.
#============================================================

# Tipagem de dados "primitivos", "especiais" etc em Python:

# region | inteiro
Variable_A = 42 
    # -> ("primitivo")
# endregion

# region | ponto flutuante (float)
Variable_B = 3.14 
    # -> ( "primitivo")
# endregion

# region | boolean (booleano/estado)
Variable_C = True 
    # -> ("primitivo")
# endregion

# region | complex (número complexo)
Variable_D = 5 + 3j 
    # -> Complex (A soma/subtração de um número real a um imaginário, "primitivo")
# endregion

# region | Nonetype
Variable_E = None 
    # -> (Representa a ausência de valor [o null de outras linguagens], "especial")
# endregion

# region | struct
from dataclasses import dataclass
@dataclass
class StructPessoa: nome: str; idade: int
    # -> Struct (Estrutura): Agrupamento de diferentes tipos de dados sob um único molde, não sendo, dessa forma, uma coleção, mas um dado único.
    # Serve para criar um "formulário" personalizado onde cada campo reconhecido pela dataclass tem um nome e uma anotação de tipo; essa anotação não impõe o tipo automaticamente em runtime.
# endregion

# region | ponteiro
Variable_N = id(Variable_A) 
    # -> Pointer/Reference (Endereço): Representa, na memória, a localização de um dado na memória.
    # ============================================
    # Nesse caso nós estamos verificando o endereço de memória (através da função id()) que a Variable_A está armazenando. em CPython, id(objeto) normalmente corresponde ao endereço de memória do objeto.
    # =============================================
    # Em Python, não manipulamos o ponteiro diretamente, somente podemos acessar o endereço de memória através da função id().
    # Toda variável é uma referência (ponteiro) que aponta para um objeto.
# endregion

# region | Union
# Union (União de Tipos):
    # Não armazena dados e nem é um dado em si; é um Metadado (um dado sobre outro dado, cuja função aqui é indicar tipo [type hinting]).
    # Explicita que um Identificador (parâmetro ou variável) é esperado como uma entre mais de uma espécie de objeto.

# Exemplo:
def funcao(dado: int | str): 
    # -> O ':' seguido de 'int | str' etiqueta o parâmetro: é a PROMESSA de tratamento desses tipos.

    # Triagem (Ação):
    if isinstance(dado, int): 
        # O interpretador confirma o tipo do objeto para aplicar a ferramenta correta.
        return dado + 1
    
    # Considerando respeitada a anotação int | str, o "else" é o único caminho restante: se não é int, só pode ser str.
    return f"Você digitou uma string: {dado.upper()}"

    # isinstance(objeto, tipo) -> Função de checagem (triagem); essencial para refinar o comportamento baseado no tipo real do objeto, permitindo que o código execute comportamentos diferentes para cada tipo, evitando operações incompatíveis com o tipo do objeto.
# endregion
# Dado:
    # É (literalmente) qualquer informação, valor.

# Conceitos relacionados:
    # Definição de variáveis: 
        # são nomes que referenciam dados dentro de um contexto (escopo).
        # Extra: elas permitem que armazenemos valores e os utilizemos/manipulemos posteriormente, sem que o python realize a operação e depois esqueça o resultado.

    # Escopo:
        # É o ambiente no qual identificadores (nomes/variáveis) podem ser reconhecidos e acessados.
        # O escopo determina a visibilidade desses identificadores dentro do programa,
        # podendo ser global ou local.
#=======================================================

# Nuances importantes: 
    # tudo em python é um objeto, mas para fins didáticos podemos classificá-los como dados primitivos, especiais etc.

    # Python é uma linguagem de tipagem dinâmica e forte, ou seja: 
        # respectivamente, quem tem tipo é o valor (objeto), a variável é só uma referência que aponta para algo tipado e a linguagem Não permite misturar tipos sem conversão explícita, evita ambiguidades.

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

# region | decimal (float)
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
    # Serve para criar um "formulário" personalizado onde cada campo tem um nome e um tipo definido.
# endregion

# region | ponteiro
Variable_N = id(Variable_A) 
    # -> Pointer/Reference (Endereço): Representa, na memória, a localização de um dado na memória.
    # ============================================
    # Nesse caso nós estamos verificando o endereço de memória (através da função id()) que a Variable_A está armazenando.
    # =============================================
    # Em Python, não manipulamos o ponteiro diretamente, somente podemos acessar o endereço de memória através da função id(), mudando o apontamento. 
    # Toda variável é uma referência (ponteiro) que aponta para um objeto.
# endregion

# region | Union
# Union (União de Tipos):
    # Não armazena dados e nem é um dado em si; é um Metadado (um dado sobre outro dado, cuja função aqui é indicar tipo [type hinting]).
    # Explicita que um Identificador (parâmetro ou variável) aceita mais de uma espécie de objeto.

# Exemplo:
def funcao(dado: int | str): 
    # -> O ':' seguido de 'int | str' etiqueta o parâmetro: é a PROMESSA de tratamento desses tipos.

    # Triagem (Ação):
    if isinstance(dado, int): 
        # O interpretador confirma a 'identidade' do objeto para aplicar a ferramenta correta.
        return dado + 1
    
    # O "else" (como sendo o único caminho restante) aqui é seguro porque a Union restringiu a entrada; se não é int, só pode ser str.
    return f"Você digitou uma string: {dado.upper()}"

    # isinstance(objeto, tipo) -> Função de checagem (triagem); essencial para refinar o comportamento baseado no tipo real do objeto, permitindo que o código execute comportamentos diferentes para cada tipo sem causar erros de tipagem forte.
# endregion
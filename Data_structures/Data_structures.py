# =================================
# ESTRUTURAS DE DADOS / COLEÇÕES
# =================================

# O que são estruturas de dados (ou coleções)?
    # Em Python, são formas de organizar dados para facilitar acesso e manipulação.

# Características das coleções:
# - Ordenação: existência de uma sequência previsível dos elementos (índices em muitas coleções).
# - Associação: capacidade de relacionar valores a chaves (dicionários).
# - Mutabilidade/Imutabilidade: possibilidade de alterar os dados depois de criados.
# - Duplicidade: se a estrutura permite elementos repetidos ou não.

# ======================================

# region | array
import array
Variable_O = array.array('i', [1, 2, 3]) 
    # -> Array (Vetor; Coleção ordenada, mutável e de TIPO ÚNICO).
    # Estrutura otimizada para armazenar dados homogêneos, com menor custo de memória do que listas tradicionais.
    # -> array.array(): Chama o construtor dentro do módulo para fabricar o objeto.
    # -> 'i' (Typecode): Define elementos com a representação de um signed int de C; todos têm tamanho fixo dentro do array, mas esse tamanho depende da plataforma (comumente 4 bytes).
    # -> [1, 2, 3]: Lista temporária usada apenas para "alimentar" o array com os dados iniciais.
    # -> 'import' localiza o módulo 'array' e o carrega na RAM como um objeto acessível, sem isso, o interpretador não conhece os 'Typecodes' (moldes) nem a lógica de memória contígua.
# endregion    

# region | bytearray
Variable_S = bytearray(b"hello") 
    # -> bytearray (Coleção ordenada e mutável de bytes contíguos que são interpretados como valores numéricos.)
    # Permite alterar, adicionar ou remover bytes individuais.
    # Se desejar que seja interpretado como texto, é necessário decodificar os bytes usando o método .decode() e especificar a codificação (ex: 'utf-8').
    # Muito usado em Buffers (áreas de memória que recebem dados de rede ou arquivos aos poucos)
# endregion

# region | bytes   
Variable_R = b"hello" 
    # -> bytes (Coleção ordenada e imutável de bytes contíguos que são interpretados como valores numéricos.)
    # Se desejar que seja interpretado como texto, é necessário decodificar os bytes usando o método .decode() e especificar a codificação (ex: 'utf-8')
# endregion

# region | dictionary
Variable_k = {"nome": "gemini", "versão": 3.0} 
    # -> dictionary (Coleção associativa, mutável e ordenada por inserção.)
    # Em Python moderno (3.7+) a ordem de inserção é garantida pela linguagem.
# endregion

# region | enum 
from enum import Enum
class Cores(Enum): VERMELHO = 1; AZUL = 2
    # -> Enum (Enumeração): Coleção ordenada e imutável de membros (nomes simbólicos) vinculados a valores constantes (imutáveis).
    # - Unicidade: Os nomes dos membros são únicos; não podem existir dois nomes iguais no mesmo Enum.
    # - Categorização: Serve para definir um conjunto fixo de opções de atribuição de significado, impedindo o uso de valores arbitrários ou números sem significado no código.
    # Diferente de um dicionário (que é uma estrutura de dados dinâmica [Passível a crescimento durante execução do código]), o Enum define um novo "Tipo" de dado (Type).
    # Por ser estático e imutável, sua estrutura e valores não podem ser alterados após a definição.
# endregion

# region | frozenset  
Variable_M = frozenset([1, 2, 3]) 
    # -> frozenset (coleção não ordenada de elementos únicos [não duplicados] e imutável
# endregion
    
# region | list
Variable_i = [1, 2, 3] 
    # -> list (coleção ordenada mutável
# endregion

# region | set
Variable_L = {1, 2, 3, 3, 3} 
    # -> set/conjunto (coleção não ordenada de elementos únicos [não duplicados] e mutável)
# endregion

# region | string   
Variable_A = "hello world" 
    # -> str (coleção ordenada e imutável de caracteres Unicode.)
    # Internamente, esses caracteres precisam ser codificados em bytes
    # para armazenamento e processamento pelo computador.

    # Representa texto ou símbolos interpretáveis pelo ser humano.

    # Didaticamente, pode ser vista como o "átomo" do texto em Python,
    # já que a linguagem não possui um tipo Char separado para representar
    # um único caractere individualmente.
# endregion
    
# region | tuple
Variable_j = (1, 2, 3) 
    # -> tuple (coleção ordenada imutável)
# endregion
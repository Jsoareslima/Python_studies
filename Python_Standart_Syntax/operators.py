# ==========================================================
# OPERADORES EM PYTHON
# ==========================================================

# Operadores são símbolos ou palavras que realizam operações
# sobre valores (operandos).
#
# Exemplo:
# 10 + 5
#
# "+" é o operador
# 10 e 5 são os operandos
 
# Operadores que ainda preciso organizar: identidade, pertencimento, ternário e bitwise.
# Áreas de detalhes que preciso organizar: precedência dos operadores e pegadinhas comuns.

#===========================================================

# OBS: tipos incompatíveis não são convertidos arbitrariamente só para uma operação funcionar; alguns tipos compatíveis possuem operações/conversões definidas entre si.

#===========================================================

# region | Operadores aritméticos ✅

    # region | Definição

        # utilizados para realizar cálculos matemáticos.

    # endregion
    # region | Dados para a exemplificação feita mais abaixo
    
        # a = 10
        # b = 3

# endregion
    # region | Soma
    
        # print(a + b)      -> 13

    # endregion
    # region | Subtração
    
        # print(a - b)      -> 7

    # endregion
    # region | Multiplicação
    
        # print(a * b)      -> 30

    # endregion
    # region | Divisão comum (sempre retorna float)
    
        # print(a / b)      -> 3.3333333333333335

    # endregion
    # region | Divisão pelo piso (floor division: divide e arredonda o resultado para baixo)

        # print(a // b)     -> 3

    # endregion
    # region | Módulo (retorna o resto associado à divisão pelo piso; o resultado não precisa ser int)
    
        # print(a % b)      -> 1

    # endregion
    # region | Potenciação

        # print(a ** b)     -> 1000 (10³)

    # endregion
    # region | Prioridade usando parêntesis
    
        # print((a + b) * 2)  -> 26

    # endregion

# endregion

# region | Operadores de comparação ✅

    # region | Definição 

        # sempre retornam True ou False.

        # Muito usados em:
        # - if
        # - while
        # - validações

    # endregion
    # region | Igual

        # print(a == b)      False -> Igual

    # endregion      
    # region | Diferente
        
        # print(a != b)      True  -> Diferente

    # endregion 
    # region | Maior

        # print(a > b)       True  -> Maior

    # endregion
    # region | Menor

        # print(a < b)       False -> Menor

    # endregion
    # region | Maior ou igual

        # print(a >= b)      True  -> Maior ou igual

    # endregion
    # region | Menor ou igual

        # print(a <= b)      False -> Menor ou igual

    # endregion
    # region | Dados para exemplificação, feita agora

        # idade = 18
        # print(idade >= 18)  True

    # endregion

# endregion

# region | Operadores lógicos ✅

    # region | Definição

        # utilizados para combinar condições.
        # Truthy/Falsy descreve como um objeto se comporta em contexto booleano:
        # bool(objeto) -> True = truthy; bool(objeto) -> False = falsy.

    # endregion
    # region | Dados para a exemplificação feita mais abaixo
         
        # idade = 20
        # tem_carteira = True

    # endregion
    # region | AND:

        # Só é considerado verdadeiro se TODOS os operandos avaliados forem truthy.
        # Retorna o primeiro valor falsy encontrado ou, se todos forem truthy,
        # retorna o último valor avaliado.

    # endregion
    # region | OR:

        # É considerado verdadeiro se PELO MENOS UM operando for truthy.
        # Retorna o primeiro valor truthy encontrado ou, se todos forem falsy,
        # retorna o último valor avaliado.

    # endregion 
    # region | NOT:

        # avalia a truthiness do operando e sempre retorna o bool oposto.

        # print(not tem_carteira)
        # False

        # Exemplo prático
        # chuva = False
        # guarda_chuva = True

        # print(chuva and guarda_chuva)
        # False

    # endregion

# endregion

# region | Operadores de atribuição ✅
    # region | Definição

        # servem para armazenar ou atualizar valores.
        # Com tipos imutáveis simples, x += y pode ser lido conceitualmente como x = x + y.
        # Porém, operadores compostos também podem executar uma operação in-place e modificar o próprio objeto quando o tipo permite.

    # endregion
    # region | +=

        #  soma o elemento da esquerda ao da direita
        # depois da igualdade:

            # x = x + 5
            # para um int, equivale a: x += 5

    # endregion
    # region | *=

        # multiplica o elemento da esquerda ao da direita
        # depois da igualdade:

            # x = x * 5
            # para um int, equivale a: x *= 5

    # endregion
    # region | -=

        # subtrae o elemento da esquerda ao da direita
        # depois da igualdade:

            # x = x - 5
            # para um int, equivale a: x -= 5

    # endregion
    # region | /=

        # divide o elemento da esquerda ao da direita
        # depois da igualdade:

            # x = x / 5
            # para um int, equivale a: x /= 5

    # endregion
    # region | //=

        # faz divisão pelo piso, do elemento da esquerda pelo da direita
        # depois da igualdade:

            # x = x // 5
            # para um int, equivale a: x //= 5

    # endregion
    # region | %=

        # calcula o módulo (resto associado à divisão pelo piso) do elemento da esquerda pelo da direita
        # depois da igualdade:

            # x = x % 5
            # para um int, equivale a: x %= 5

    # endregion
    # region | **=

        # potencia o elemento da esquerda ao da direita
        # depois da igualdade:

            # x = x ** 5
            # para um int, equivale a: x **= 5

    # endregion

# endregion



# region | Operadores de identidade 📍 

# Verificam se duas variáveis apontam para o MESMO objeto
# na memória.
#
# NÃO confundir com "==".
#
# == compara VALORES
# is compara IDENTIDADE
#

lista1 = [1, 2]
lista2 = lista1

print(lista1 is lista2)
# True

print(lista1 is not lista2)
# False

# Exemplo mostrando a diferença

a = [1, 2]
b = [1, 2]

print(a == b)
# True (mesmos valores)

print(a is b)
# False (objetos diferentes)

# endregion

# region | Operadores de pertencimento 📍

# Verificam se um valor pertence a um objeto que suporta teste de pertencimento
# (lista, string, tupla, set, dict, etc.).

lista = [1, 2, 3, 4]

print(1 in lista)
# True

print(5 not in lista)
# True

texto = "Python"

print("P" in texto)
# True

print("Java" in texto)
# False

# endregion

# region | Operador ternário 📍

# Forma compacta de escrever um if/else simples.

# Sintaxe:
# valor_se_verdadeiro if condição else valor_se_falso

idade = 20

resultado = "Maior de idade" if idade >= 18 else "Menor de idade"

print(resultado)

# Equivale a:

if idade >= 18:
    resultado = "Maior de idade"
else:
    resultado = "Menor de idade"

# endregion

# region | Operadores bitwise (binários) 📍

# Trabalham diretamente sobre os bits de números inteiros.
# Assunto mais avançado.

# Muito utilizado em:

# - Sistemas embarcados
# - Redes
# - Criptografia
# - Manipulação de permissões

# Normalmente não são necessários para iniciantes.

a = 5  # 101
b = 3  # 011

print(a & b)   # AND binário
print(a | b)   # OR binário
print(a ^ b)   # XOR binário
print(~a)      # NOT binário
print(a << 1)  # Shift à esquerda
print(a >> 1)  # Shift à direita

# endregion

# region | Precedência dos operadores 📍

# Ordem simplificada:

# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. Comparações
# 6. not
# 7. and
# 8. or

# Exemplo:

resultado = 2 + 3 * 4

print(resultado)
# 14
#
# Primeiro:
# 3 * 4 = 12
#
# Depois:
# 2 + 12 = 14

# endregion

# region | Pegadinhas comuns 📍

# 1. Divisão sempre retorna float
print(10 / 2)   # 5.0

# 2. "==" NÃO é a mesma coisa que "="

x = 10      # atribuição
print(x == 10)  # comparação

# 3. "is" NÃO substitui "=="

a = [1]
b = [1]

print(a == b)  # True
print(a is b)  # False

# 4. Strings também aceitam operadores

print("Py" + "thon")  # Python
print("Ha" * 3)       # HaHaHa

# endregion



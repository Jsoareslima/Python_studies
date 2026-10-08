
# Função não nomeada (Lambda):
    # é uma função criada com a expressão lambda, sem uma declaração def.
    # Pode ser usada diretamente ou associada a um nome.
    # É geralmente usada para comportamentos curtos.
    # Seu corpo é limitado a uma única expressão.
#-----//--------//------------//----------//----------//-----------//---------/

# region | Exemplo de função lambda (com argumento e parâmetro):

somar = lambda a, b: a + b

resultado = somar(2, 3)

print(resultado)

# OBS 1: Funções lambda possuem retorno implícito:
    # a única expressão permitida na lambda
    # é automaticamente retornada como resultado da função.

# OBS 2:
    # Uma lambda é um objeto função, assim como uma função criada com def.
    
    # somar -> referência para a função.
    # somar() -> chamada da função
    
    # Por ser um objeto, uma função lambda pode ser:

        # Associada a uma variável

        # Passada como argumento para outra função.
            # def aplicar_operacao(funcao, a, b):
            #     return funcao(a, b)

            # resultado = aplicar_operacao(
            #     lambda x, y: x + y,
            #     2,
            #     3
            # )

            # print(resultado) -> 5

            # lambda x, y: x + y
            #   |
            #   V
            # é o argumento recebido pelo parâmetro "funcao"

        # Retornada por outra função.

        # Chamada mais de uma vez.

# OBS 3: 
    # Lambdas aparecem com frequência em funções que recebem outras funções como argumentos. Como no exemplo abaixo:

    # numeros = [1,2,3,4]

    # dobrados = map(lambda x: x * 2, numeros)
    # pares = filter(lambda x: x % 2 == 0, numeros)
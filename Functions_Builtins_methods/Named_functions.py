
# Função nomeada:
    # Definição
        # É um bloco reutilizável de código associado a um identificador (nome).
        # A função encapsula instruções que podem realizar
        # uma tarefa específica, executando-as quando é chamada.

    # Argumento:
        # É o valor, objeto ou referência (variável) fornecida a uma função
        # no momento em que ela é chamada.

    # Parâmetro:
        # É uma variável local definida na assinatura da função (a interface estrutural declarativa da função), responsável por receber o valor/referência do argumento.
#-----//--------//------------//----------//----------//-----------//---------//

# region | Exemplo sem parâmetros:
def saudacao():

    print("Olá")
    print("Bem-vindo ao sistema")
    print("Função executada com sucesso") # -> A função pode conter múltiplas expressões/instruções internas.


saudacao() # -> Chamada da função:
# endregion

# region | Passagem de argumento para uma função (com parâmetro):
def saudacao(nome):

    print(f"Olá {nome}")

saudacao("Carlos") # -> Chamada da função:
# endregion
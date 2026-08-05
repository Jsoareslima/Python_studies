
# Função não nomeada (Lambda):
    # É uma função criada sem declaração formal de nome,
    # geralmente usada para operações curtas e rápidas.
    # Em Python, funções lambda permitem apenas uma única expressão,
    # não múltiplas instruções ou blocos de execução.
#-----//--------//------------//----------//----------//-----------//---------/

# region | Exemplo de função lambda (com argumento e parâmetro):

somar = lambda a, b: a + b

resultado = somar(2, 3)

print(resultado)

# OBS: Funções lambda possuem retorno implícito:
    # a única expressão permitida na lambda
    # é automaticamente retornada como resultado da função.
# endregion
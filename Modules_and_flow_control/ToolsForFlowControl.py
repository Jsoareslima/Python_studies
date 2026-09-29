# Ferramentas de controle de fluxo são mecanismos lógicos, expressos pela sintaxe das linguagens de programação, responsáveis por definir como a execução de um programa ocorrerá ao longo do código.

# Existem quatro estruturas principais em Python para controle de fluxo:

# Condicionais:
# Permitem que o programa tome decisões com base em condições específicas ou sequências.
# As estruturas condicionais mais comuns são:
# if, elif, else, match/case (estrutura de pattern matching semelhante ao switch/case de outras linguagens), etc.

# Laços de repetição:
# Permitem que um bloco de código seja executado várias vezes, com base em uma condição ou percorrendo um iterável.
# As estruturas de repetição mais comuns são:
# for, while, etc.

# Controle de fluxo de exceção:
# Permite que o programa lide com erros e situações excepcionais de maneira controlada.
# As estruturas de controle de exceção mais comuns são:
# try, except, finally, raise, etc.

# Desvio de fluxo:
# Permite que o programa altere o fluxo de execução abruptamente.
# Manifestam-se através de:
# break, continue, return, etc.

#--------------------//-----------------------//-----------------//

# =========================
# CONDICIONAIS
# =========================

# if:
# Executa um bloco caso a condição seja verdadeira. Busca a verdade ou falsidade de uma expressão, não trabalha com similaridades ou padrões.

idade = 18

if idade >= 18:
    print("Maior de idade")


# elif:
# Testa uma nova condição caso a anterior seja falsa.

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")


# else:
# Executa um bloco caso nenhuma condição anterior seja verdadeira.
# Cria um caminho alternativo exclusivo baseado na avaliação booleana das condições anteriores.

temperatura = 35

if temperatura < 15:
    print("Frio")
else:
    print("Quente")


# match/case:
# Compara padrões/valores de maneira organizada
# O "case _:"" quer dizer -> qualquer outra coisa.
# trabalha principalmente com reconhecimento de padrões estruturais - perguntando: "isso combina com essa estrutura?" se sim ele executa o bloco de código correspondente.

comando = "salvar"

match comando:
    case "abrir":
        print("Abrindo arquivo")
    case "salvar":
        print("Salvando arquivo")
    case "fechar":
        print("Fechando programa")
    case _:
        print("Comando desconhecido")


# =========================
# LAÇOS DE REPETIÇÃO
# =========================

# for:
# Repete um bloco percorrendo um iterável.

for numero in [1, 2, 3]:
    print(numero)


# while:
# Repete enquanto a condição for verdadeira.

contador = 0

while contador < 3:
    print(contador)
    contador += 1


# =========================
# CONTROLE DE EXCEÇÃO
# =========================

# try / except / finally:
# try delimita o bloco protegido. Ele precisa estar associado a pelo menos um except ou finally; o except captura/trata exceções, enquanto o finally executa ao final da estrutura independentemente de erro ter ocorrido ou não.

# É possível capturar múltiplos tipos de erros chamando as classes que representam esses erros no except, como no exemplo abaixo.

try:
    numero = int("10")
    print(numero)
except ValueError: # -> Poderia ter sido um TypeError, IndexError etc.
    print("Valor inválido")
finally:
    print("Fim da operação")

# raise:
# Lança uma exceção manualmente para indicar que uma situação inválida,
# inesperada ou não suportada ocorreu durante a execução do programa.

idade = -5

if idade < 0:
    raise ValueError("Idade não pode ser negativa")


# =========================
# DESVIO DE FLUXO
# =========================

# break:
# Interrompe completamente um laço.

for numero in range(10):

    if numero == 5:
        break

    print(numero)


# continue:
# Pula apenas a iteração atual (e com isso ignora o restante do código dentro do laço para aquela iteração específica, mas continua com as próximas iterações normalmente).

for numero in range(5):

    if numero == 2:
        continue
    print(numero)


# return:
# return encerra a execução da função e transfere o resultado processado, para o ponto do código que realizou a chamada da função (normalmente uma variável), tornando esse resultado acessível ao restante do programa.
# 
# A função processa dados dentro de seu escopo local.

def somar(a, b):
    return a + b

resultado = somar(2, 3)

print(resultado)


# =========================
# INSTRUÇÃO NULA / PLACEHOLDER
# =========================

# pass:
# Não desvia o fluxo: é uma instrução nula, usada como placeholder (algo que ocupa um lugar temporariamente até que alguma implementação real seja colocada ali).
# Mantém a estrutura sintaticamente válida mesmo sem implementação.

if True:
    pass


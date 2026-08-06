# =================================
# CONCEITOS GERAIS DE POO
# =================================

# LEGENDA:

    # ✅ -> Completo, mas sempre com espaço para aprofundamento;
    # ❌ -> Incompleto ou vazio;
    # 📍 -> Expressa necessidade de revisão, sendo completo ou não;
    # 🎯 -> meu alvo de estudos no momento;

# DETALHES:

    # Se uma region filha for ❌:
        # a region pai terá que ter essa mesma legenda, independente de ter outras filhas ✅.
        # o mesmo vale para qualquer outra legenda.

    # Se uma region pai tiver alguma legenda (✅❌🎯📍) e a(s) regions filhas tiverem a mesma legenda:
        #  Não há necessidade de repetir as legendas nas regions filhas.

# ======================================

# region | Classe ✅
    # region | Atributos 
        # region | Definição

            # são variáveis, dentro da estrutura de uma classe, associadas a uma classe ou instância, responsáveis por armazenar o estado e os dados do objeto.

        # endregion 
        # region | Atributos de instância

            # São atributos definidos dentro do __init__ via self.atributo = valor. Pertencem exclusivamente ao objeto criado — cada instância tem os seus próprios, independentes das demais. Exemplo:

            # class Carro:
            #   def __init__(self, cor):
            #       self.cor = cor  # cada carro tem sua própria cor

            # carro1 = Carro("vermelho")
            # carro2 = Carro("azul")

            # carro1.cor e carro2.cor são independentes

        # endregion
        # region | Atributos de classe

            # São atributos definidos diretamente no corpo da classe, fora de qualquer método. São compartilhados entre todas as instâncias — se alterado na classe, todas as instâncias    sofrerão a mudança. Exemplo:

            # class Carro:
            #     rodas = 4  -> todas as instâncias compartilham esse valor

            # carro1 = Carro()
            # carro2 = Carro()
            # carro1.rodas e carro2.rodas são ambos 4

            # OBS: apesar de todas as instâncias criadas a partir da classe compartilharem um mesmo atributo de classe, não há qualquer relação de sincronismo entre as instâncias, elas somente compartilham um mesmo atributo de classe inicial.

        # endregion
    
    # endregion
    # region | Métodos 
        # region | Definição

            # é uma função definida dentro de uma classe.
            # Normalmente utilizada para manipular
            # ou operar sobre os dados da instância. Exemplo:

            # class Personagem:
                # def __init__(self, nome, vida):
                    # self.nomeDoPersonagem = nome
                    # self.vidaDoPersonagem = vida
                # def atacar(self): -> método
                    # print(f"{self.nomeDoPersonagem} atacou!")

        # endregion
        # region | Métodos de instância

            # - são métodos que recebem automaticamente a referência ao próprio objeto (self) como primeiro argumento. Isso significa que eles têm acesso direto ao estado daquela instância específica — podem ler e modificar seus atributos. É o tipo padrão de método em uma classe, usado sempre que a operação depende dos dados do objeto.

            # class ContaBancaria:
            #     def __init__(self, saldo):
            #         self.saldo = saldo

            #     def depositar(self, valor):  -> método de instância
            #         self.saldo += valor      -> acessa e modifica o estado da instância

        # endregion  
        # region | Métodos especiais (dunder methods)
            # region | Definição

                # métodos que possuem nomes com prefixo e sufixo "__", sendo disparados automaticamente pelo Python, em eventos específicos ou operações nativas (como print, () ou +). Implementam comportamentos específicos a objetos.

            # endregion
            # region | Método inicializador (__init__):

                # é um método especial executado automaticamente
                # após a criação da instância na memória, se declarado.
                # sendo responsável por inicializar/configurar
                # o estado inicial do objeto.

                # OBS 1.0:
                    # o método inicializador (__init__) não cria a instância,
                    # a criação do objeto acontece durante a execução do programa,
                    # no momento em que a classe é chamada, como descrito abaixo:

                    # o Python cria uma nova instância (instanciação)
                    # na memória, utilizando outro método especial, e somente depois executa o método inicializador (inicialização) que irá configurar o objeto, se ele foi declarado.

            # endregion
            # region | Método de representação (__str__):

                # é um método especial que define como o objeto deve ser 
                # representado em formato de string (texto).
                # é acionado automaticamente quando usamos print() ou str()
                # no objeto, permitindo uma visualização mais amigável
                # dos dados em vez do endereço de memória.

            # endregion
        
        # endregion 
        # region | Métodos de classe

            # são definidos com decoradores (@classmethod), Decoradores são um conceito separado — ver módulo específico.

        # endregion
        # region | Métodos estáticos 

            # são definidos com decoradores (@staticmethod), Decoradores são um conceito separado — ver módulo específico.

        # endregion   

    # endregion

# endregion
# region | Instância/objeto ✅
    # region | Definição

        # é um objeto criado a partir da estrutura (atributos de classe/instância, métodos etc) definida pela classe.

    # endregion
    # region | Estado da instância/objeto:

        # é o conjunto atual de dados/valores
        # armazenados nos atributos da instância
        # durante a execução do programa.

    # endregion
    # region | Self
        # region | Definição

            # Quando um método de instância é chamado, Python passa o próprio objeto como primeiro argumento automaticamente — você nunca escreve esse argumento, ele é injetado. self é o parâmetro que recebe essa referência, permitindo que o método leia e modifique os atributos daquele objeto específico. Por convenção se chama self, mas poderia ter qualquer nome. 

            # Existe independentemente do método inicializador.

            # exemplo: 

            # o parâmetro "nome" recebe o argumento fornecido
            # durante a criação da instância
            # e seu valor é atribuído ao atributo do objeto.
            
            # class Pessoa:
                # def __init__(self, nome):
                    # self.atributo_do_objeto = nome 
   
        # endregion 
        
    # endregion
    # region | formas de instanciar um objeto

        # Existem diversas formas de criar um objeto.

        # OBS: 
            # Independentemente da forma utilizada, toda
            # instanciação de uma classe normalmente passa pelo
            # processo de:
            
            # 1. __new__  -> cria o objeto.
            # 2. __init__ -> inicializa o objeto.

        # region | Instanciação direta (mais comum)

            # O próprio nome da classe é chamado como uma função.
            
            # class Pessoa:
            #     ...
            
            # p = Pessoa()

        # endregion
        # region | Através de uma função (Factory Function)

            # Uma função cria e retorna uma instância.
            
            # def criar_pessoa(nome):
            #     return Pessoa(nome)
            
            # p = criar_pessoa("Victor")

        # endregion
        # region | Através de um método de classe (Factory Method)

            # Um método marcado com @classmethod cria e retorna
            # uma nova instância da própria classe.
            
            # class Pessoa:
            #
            #     @classmethod
            #     def anonima(cls):
            #         return cls("Anônimo")
            
            # p = Pessoa.anonima()

        # endregion
        # region | Sobrescrevendo __new__

            # __new__ é responsável por criar o objeto antes de
            # __init__ inicializá-lo. É utilizado em casos
            # especiais, como tipos imutáveis, singletons ou
            # controle da criação de instâncias.
            
            # class Pessoa:
            #     def __new__(cls):
            #         return super().__new__(cls)

        # endregion
        # region | Copiando um objeto existente

            # Em vez de criar um objeto "do zero", pode-se criar
            # uma nova instância copiando outra.
            
            # import copy
            
            # p2 = copy.copy(p1)      # cópia rasa
            # p3 = copy.deepcopy(p1)  # cópia profunda

        # endregion
        # region | Desserialização

            # Alguns módulos recriam objetos a partir de arquivos,
            # bytes ou texto.
            
            # import pickle
            
            # objeto = pickle.load(arquivo)

        # endregion

    # endregion

    # endregion
# endregion
# region | Herança ❌

    # Herança é um mecanismo pelo qual uma nova classe (classe filha ou subclasse) é construída a partir de uma classe existente (classe pai ou superclasse), passando automaticamente a possuir todos os atributos e métodos definidos na classe pai, podendo ainda adicionar novos comportamentos ou modificar os existentes.

    # region | Classe pai (superclasse): ✅

        # É a classe utilizada como base para a criação de uma ou mais subclasses.
        # Em Python, uma classe torna-se uma superclasse quando outra classe herda dela.
        
        # Não existe qualquer sintaxe especial para definir uma superclasse.
        # Basta que outra classe a utilize como classe base.

    # endregion
    # region | Classe filha (subclasse): ✅

        # É uma classe criada herdando outra classe.
        
        # Em Python, uma subclasse é definida informando a classe base
        # entre parênteses na declaração da classe.
        
        # Exemplo:
        
        # class Cachorro(Animal):
        #     pass
        
        # A subclasse pode acessar os atributos e métodos herdados,
        # mas seu código contém apenas os membros que ela própria
        # declara ou sobrescreve. Os membros herdados continuam
        # pertencendo à superclasse.

# endregion
    # region | Exemplo de herança em código ✅

        # region | classe pai (superclasse):

            # class Animal:

            # especie = "Animal"

            # def __init__(self, nome):
            #     self.nome = nome

            # def respirar(self):
            #     print("Respirando")

        # endregion
        # region | classe filha (subclasse):

            # class Cachorro(Animal):

            # def latir(self):
            #     print("Au Au!")

        # endregion
        # region | detalhes 

            # Visualmente a classe filha mostra somente o método que ela mesma possui, mas ela pode fazer tudo isso descrito abaixo:

            # dog = Cachorro("Rex")

            # print(dog.especie)   # herdado

            # print(dog.nome)      # herdado

            # dog.respirar()       # herdado

            # dog.latir()          # declarado na subclasse

        # endregion

    # endregion
    # region | Ordem de Resolução de Métodos (Method Resolution Order - MRO) ✅

        # É a sequência ordenada (concreta) de classes da hierarquia de herança,
        # calculada automaticamente pelo Python por meio de um algoritmo
        # de linearização (C3 Linearization), que determina a ordem em que
        # atributos e métodos são procurados.
        
        # Quando um membro não é encontrado na classe atual,
        # a busca continua seguindo essa sequência até encontrá-lo
        # ou chegar à classe base object.

        # OBS: O MRO não é a categoria, nem a idealização, mas é o resultado concreto da execução do C3.

        # region | MRO + super()

            # super() é uma função built-in utilizada principalmente em herança
            # para acessar a implementação de métodos da próxima classe na Ordem
            # de Resolução de Métodos (MRO).
        
            # Ao ser chamada, super() inicia uma nova busca pelo método solicitado,
            # começando na classe seguinte à classe atual dentro da MRO. Em herança
            # simples, essa classe normalmente corresponde à classe pai; em herança
            # múltipla, ela é determinada pela própria MRO.
            
            # Ver módulo: Funções built-in -> super().

        # endregion 

    # endregion

    # region | Herança múltipla ❌
    # endregion     

# endregion

# ================================
# Conceitos mais aprofundados:
# ================================

# region | Polimorfismo ❌
    # É a capacidade de diferentes objetos
    # responderem ao mesmo método/comando
    # de maneiras diferentes.
# endregion

# region | Encapsulamento ❌
    # É o princípio de restringir/modularizar
    # o acesso direto aos dados internos de uma classe,
    # fornecendo métodos/controladores
    # para interação segura com o objeto.
# endregion

# region | classes aninhadas
    # region | composição ❌
# endregion


## 📁 Sobre a organização

Este repositório reúne meus estudos de lógica de programação aplicada a Python 
e já conta com 244+ arquivos. Manter um índice manual neste README seria 
inviável e ficaria desatualizado.

Por isso, optei por organizar o conteúdo usando **regions** (`# region` / 
`# endregion`) dentro dos próprios arquivos. Assim, basta abrir o projeto na 
sua IDE (VS Code, PyCharm etc.) e usar o recurso de recolher/expandir seções 
para navegar pelo conteúdo de forma rápida e visual.

> a maioria das IDEs reconhece os comentários `# region` do Python 
> automaticamente e permite colapsar essas seções na barra lateral ou no editor.

⚠️ **OBS:** essa organização ainda está em transição. Dependendo do arquivo, 
as regions podem não estar presentes, e alguns arquivos podem estar apenas 
parcialmente organizados (ou seja, com regions definidas só em parte do conteúdo). 
Estou ajustando isso gradualmente conforme revisito os estudos.

======================================================================

# 🎯 Quanto às region/endregions:
Foram organizadas dois tipos de estruturas.

# 1ª - Uma estrutura organizacional para regions com exemplo em código normal:
* Regions "coladas" ao bloco de código, porque o conteúdo não pode ser identado dentro do nada. Mas podendo haver espaços entre os conteúdos dentro da region. Exemplo:

        # region | inteiro
        Variable_A = 42 
        # -> ("primitivo")

        print(Variable_A)
        # endregion

* O título das regions raízes e subsequentes até o conteúdo de fato pode começar com letras maiúsculas ou minúsculas, da mesma forma o conteúdo.

# 2ª - Uma estrutura organizacional para regions com exemplo em código na forma de comentários:
* O comentário explicativo fica identado e com duas linhas em branco entre ele e a region/endregion, "suspenso". Quando há várias regions/endregions em sequência (dentro de uma region "pai" ou não) o endregion da seção anterior fica colado à region da seção posterior ou não (a depender do que torne o texto melhor de se visualizar), mas o endregion da region "pai" (que agrupa qualquer conteúdo) e das "filhas" precisa de, obrigatoriamente, uma linha de espaço em relação ao que vier acima. Exemplo:

        # region | Classe
            # region | Atributos 
                # region | Definição

                    # são variáveis, dentro da estrutura de uma classe, associadas a uma classe ou 
                    instância, responsáveis por armazenar o estado e os dados do objeto.

                # endregion 
            
            # endregion 

        # endregion 

* O título das regions raízes e subsequentes até o conteúdo de fato tem que obrigatoriamente começar com letras maiúsculas e o conteúdo obrigatoriamente com letras minúsculas (idealmente, ambas as padronizações).

# extra - Estruturas colapsadas por causa da Identação sem regions:
* Segue o mesmo padrão da 2ª estrutura.

# extra - legendas:
* Existem arquivos em que a legenda é devida, outros não, nem todos que devem ter as têm ainda, mas terão conforme for estudando.

# extra - OBS's:
* Caso venha a criar um OBS indentado (com regions ou não), o posso colocar separado de regions filhas ou pais, para dar destaque. Por exemplo:
   
        # region | Classe
            # region | Atributos

                # OBS:
                    Existem atributos de classe e os atributos e de instância, são diferentes.

                # region | Definição

                    # são variáveis, dentro da estrutura de uma classe, associadas a uma classe ou 
                    instância, responsáveis por armazenar o estado e os dados do objeto.

                # endregion 
            
            # endregion 

        # endregion 

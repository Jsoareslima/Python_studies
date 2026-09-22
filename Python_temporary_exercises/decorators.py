def log(funcao):

    def wrapper():
        print("Antes")
        funcao()
        print("Depois")

    return wrapper

@log
def ola():
    print("Olá!")



    
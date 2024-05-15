class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instacia da classe...")


    def falar(self):
        print("au au")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e azul", False)
    print(c.nome)


#c = Cachorro("Chappie", "amarelo")
#c.falar()

criar_cachorro()
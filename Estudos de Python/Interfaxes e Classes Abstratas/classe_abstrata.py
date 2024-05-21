from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando a TV")
        print("Ligada")

    def desligar(self):
        print("Desligando a TV")
        print("Desligado")

    @property
    def marca(self):
        return "LG"

class ControleARcondicionado(ControleRemoto):
    def ligar(self):
        print("ligando o Ar")
        print("Ligado")

    def desligar(self):
        print("Desligando o ar")
        print("Desligado")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleARcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)


    
class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join
        ([f'{chave}={valor}' for chave, valor in self.
        __dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **KW):
        self.cor_pelo = cor_pelo
        super().__init__(**KW)

class Ave(Animal):
    def __init__(self, cor_bico, **KW):
        self.cor_bico = cor_bico
        super().__init__(**KW)

    
class Gato(Mamifero):
    pass

class Falarmixin:
    def falar(self):
        return "Falando agora"


class Ornitorrinco(Mamifero, Ave, Falarmixin):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
       # print(Ornitorrinco.__mro__)


        super().__init__(cor_pelo = cor_pelo, cor_bico =cor_bico, numero_patas=numero_patas)


#gato = Gato(4, "Preto")
#print(gato)

ornitorrinco = Ornitorrinco(numero_patas = 7, cor_pelo="vermelho", cor_bico= "preto")
print(ornitorrinco)
print(ornitorrinco.falar())
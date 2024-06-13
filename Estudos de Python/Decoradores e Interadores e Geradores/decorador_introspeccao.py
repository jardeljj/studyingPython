import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        result = funcao(*args, **kwargs)
        return result

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá Mundo! {nome}")
    
print(ola_mundo.__name__)
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        result = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return result

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá Mundo! {nome}")
    return nome.upper()
    
result = ola_mundo("Jardel")
print(result)
print(ola_mundo.__name__)
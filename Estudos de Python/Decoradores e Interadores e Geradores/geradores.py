def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[3,4,6]):
    print(i)

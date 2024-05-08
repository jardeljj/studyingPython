lista = set( [1,2,1,3,4,2,1,])

print(lista)

fruta = set("abacaxi")

print(fruta)

numeros = {1,2,3,4}

numeros = list(numeros)

print(numeros[0])

carros = {"gol", "Celta", "Jetta"}

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

    
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
junto = conjunto_a.intersection(conjunto_b)
print(junto)

a = conjunto_a.difference(conjunto_b)
b = conjunto_b.difference(conjunto_a)

print(a,b)

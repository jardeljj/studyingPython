def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Lista inicial
lista = [5, 2, 7, 1, 9]

print("Lista original:", lista)

# Chamada da função para ordenar a lista
bubble_sort(lista)

print("Lista ordenada do maior para o menor:", lista)

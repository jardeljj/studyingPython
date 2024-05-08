def somar(a, b):
    return a + b




def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)  # O resultado da operação 10 + 10 = 20

op = subtrair 

print(op(1,23))

salario = 2000

#Escopo global

def salario_bonus(bonus):
   global  salario
   salario += bonus
   return salario

total = salario_bonus(500)
print("Salario a receber é = ", total)

print()
print()


def salario_bonus(bonus, lista):
    global  salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
total = salario_bonus(500, lista)
print("Salario a receber é = ", total)
print(lista)
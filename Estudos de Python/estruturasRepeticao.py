texto = input("informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
   
print()
print()

for numero in range(0, 61, 6):
    print (numero, end=" ")

print()
print()

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] sair \n:"))

    if opcao == 1:
        print("Dinheiron Sacado")
    elif opcao == 2:
        print("Exibindo o extrato")

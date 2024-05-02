def sacar(valor = 0.0):
    saldo = 500.0
    if saldo > valor:
        print("Valor de ",valor," retirado")
        print("restou: ", saldo-valor)
    else:
        print("Saldo insuficiente")

def depositar(valor = 0):
    saldo = 500
    if valor > 0.1:
        print("Recebido o valor depositado")
        print("Total: ", saldo+valor)
    else:
        print("Erro ao efetuar o deposito")
saque = float(input("Digite o valor do saque: "))
deposito = float(input("Digite o valor de deposito: "))

sacar(saque)
depositar(deposito)

# by Jardel

menu_opcoes = """

[A] Depositar
[B] Sacar
[C] Extrato
[D] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu_opcoes)

    if opcao == "A":
        valor = float(input("Digite o valor do para o deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro ao efetuar o deposito")

    elif opcao == "B": 

        valor = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falha")
    
    elif opcao == "C":
        print("\n**************** EXTRATO ***********1******")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("********************************************")

    elif opcao == "D":
        print("Saindo")
        break
    
    else: 
     print("Operação invalida, por favor selecione novamente a operação desejada.")
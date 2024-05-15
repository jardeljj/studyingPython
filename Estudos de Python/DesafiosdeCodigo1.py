def recomendar_plano (consumo):
    if consumo <= 10:
      return 'Plano Essencial Fibra - 50Mbps'
      
    elif consumo > 10 and consumo <= 20:
      return 'Plano Prata Fibra - 100Mbps'

    elif consumo > 20:
      return 'Plano Premium Fibra - 300Mbps'

consumo = float(input("Digite o valor"))
# Chama a função recomendar_plano com 


num_elementos = 3

itens = []
for item in range (num_elementos):
   item = input("Digite o valor:")
   itens.append(item)

print("A lista criada é:", itens)
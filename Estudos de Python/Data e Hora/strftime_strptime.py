from datetime import datetime 

data_hora_atual = datetime.now()

data_hora_string = '2024-6-26 14:24'

#mascara formato Brasil
mascara_ptbr = "%d/%m/%Y %a"
#mascara formato Americano
mascara_en = '%Y-%m-%d %H:%M'

#convertendo a data para o formato de data do Brasil
print(data_hora_atual.strftime(mascara_ptbr))

#Convertendo a data para o formato amaricano
data_convertida = datetime.strptime(data_hora_string, mascara_en )
print(data_convertida)
print(type(data_convertida))
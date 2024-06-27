import os
import shutil
from pathlib import Path 

ROOT_PATH = Path(__file__).parent
#print(ROOT_PATH)

# Criando diretorio dentro do diretorio
#os.mkdir(ROOT_PATH / 'novo-diretorio')

# criando arquivo novo.txt dentro da pasta
#arquivo = open(ROOT_PATH / "novo.txt", "w")
#arquivo.close()

#Renomeando o arquivo criado
#os.rename(ROOT_PATH/"novo.txt", ROOT_PATH / "alterado.txt")

# Removendo arquivo
#os.remove(ROOT_PATH/'alterado.txt')

# Movendo arquivo para outro diretorio dentro do diretorio
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

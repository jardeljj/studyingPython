from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "loram.txt", "r") as arquivo:
    print("trabalhando com o arquivo")

# Criando arquivo 
#     with open(ROOT_PATH / 'arquivo-utf-8.txt', 'w', encoding='utf-8') as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando python")
# except IOError:
#     print("Erro ao abrir o arquivo")

#Lendo arquivo
try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print("Erro ao abrir o arquivo")
except UnicodeDecodeError as exc:
    print("erro Letra de maluco")
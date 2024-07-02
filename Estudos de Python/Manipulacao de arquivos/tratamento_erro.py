from pathlib import Path

ROOT_PATH = Path(__file__).parent
try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)
except PermissionError as exc:
    print(f"voce não tem permissão")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema aconteceu na abertura do arquivo: {exc}")

arquivo.close()
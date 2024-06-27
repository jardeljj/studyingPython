arquivo = open("C:\\Users\\Jardel\\Documents\\GitHub\\studyingPython\\Estudos de Python\\Manipulacao de arquivos\\teste.txt", "w")


arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n","Escrevendo","\n", "um","\n", "novo", "\n", "texto"])
arquivo.close()
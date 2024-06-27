arquivo = open("C:\\Users\\Jardel\\Documents\\GitHub\\studyingPython\\Estudos de Python\\Manipulacao de arquivos\\loram.txt", "r")

print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# for line in arquivo.readline():
#     print(line)

#dica:
while len(line := arquivo.readline()):
    print(line)

arquivo.close()


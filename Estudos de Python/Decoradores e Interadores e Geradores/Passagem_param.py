def mensagem(nome):
    print('executando mensagem')
    return f'oi {nome}'

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)

print(executar(mensagem, 'Jardel'))
print(executar(mensagem_longa, 'Jardel'))
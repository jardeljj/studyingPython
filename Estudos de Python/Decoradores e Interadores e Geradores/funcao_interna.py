def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print ("Executando função interna")

    def funcao_2():
        print("Executando a funcao 2")
    
    funcao_interna()
    funcao_2()

principal()

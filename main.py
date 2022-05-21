def maquina(num_pecas, peso_pecas):
    peso_total = num_pecas * peso_pecas
    if num_pecas <= 6 and peso_total <= 60:
        print("Máquina liberada")
    else:
        print("Máquina bloqueada")

num_pecas = int(input("Digite o número de peças: "))
peso_pecas = float(input("Digite o peso de cada peça: "))
maquina(num_pecas, peso_pecas)
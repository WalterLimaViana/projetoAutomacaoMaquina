sair = False
def liberarMaquina(num_pecas, peso_pecas):
    peso_total = num_pecas * peso_pecas
    if num_pecas <= 6 and peso_total <= 60:
        msg = "Máquina liberada!"
    else:
        msg ="Máquina bloqueada!"
    return msg
while True:

    conf = False

    num_pecas = int(input("Digite o número de peças: "))
    peso_pecas = float(input("Digite o peso de cada peça: "))
    msg = liberarMaquina(num_pecas, peso_pecas)

    print(msg)

    while conf == False:

        cont = input("Deseja continuar com a produção (s/n): ").lower()

        if cont == 's':
            conf = True
            continue
        elif cont == 'n':
            conf = True
            sair = True
        else:
            print("Opção inválida")

    if sair == True:
        break
    else:
        continue

print("Produção encerrada")


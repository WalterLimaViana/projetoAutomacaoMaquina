sair = False
producao = 0
def liberarMaquina(num_pecas, peso_pecas):
    global producao, peca_extra, peso_extra
    peso_total = num_pecas * peso_pecas
    if num_pecas <= 6 and peso_total <= 60:
        msg = "Máquina liberada!"
        producao = producao + 1
        peca_extra, peso_extra = 0, 0
    else:
        if num_pecas > 6:
            peca_extra = num_pecas - 6
            if peso_total > 60:
                peso_extra = peso_total - 60
            else:
                peso_extra = 0
        else:
            peso_extra = 0
            peso_extra = peso_total - 60

        msg = "Máquina bloqueada"

    return msg, producao, peca_extra, peso_extra

while True:

    conf = False

    num_pecas = int(input("Digite o número de peças: "))
    peso_pecas = float(input("Digite o peso de cada peça: "))
    msg, producao, peca_extra, peso_extra = liberarMaquina(num_pecas, peso_pecas)

    print(msg)
    if peca_extra > 0:
        print(f'Devido ao excesso de peças: {peca_extra} pç')
    if peso_extra > 0:
        print(f'Devido ao excesso de peso: {peso_extra} Kg')

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

print("="*20)
print("Produção encerrada")
print(f'A máquina produziu {producao} ciclos de peças')
print("="*20)

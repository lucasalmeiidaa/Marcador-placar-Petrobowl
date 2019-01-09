# Script para marcar o placar Petrobowl UFAM (Válido para 2 equipes)
#Para input de equipe: 1 - Equipe um, 2- Equipe dois e 0 - Nenhuma equipe.
#Autor: Lucas Evangelista de Almeida
#Versão 1.1

pts_time1 = [] #Lista para conter os pontos das questões toss-up da equipe 1.
pts_time2 = [] #Lista para conter os pontos das questões toss-up da equipe 2.
bonus_time1 = [] #Lista para conter os pontos das questões bônus da equipe 1.
bonus_time2 = [] #Lista para conter os pontos das questões bônus da equipe 2.

print("\n \n ############################## PLACAR PETROBOWL 1.1 ############################## \n \n")
rodada = 1 #Variável que armazena número da rodada.
numero_rodadas = int(input("Quantas rodadas irá ter? ")) #Variável para estipular o número de loops.
while (len(pts_time1) + len(pts_time2)) < numero_rodadas: #Loop enquanto a soma do tamanho das duas listas de tossups forem <= rodadas.
    print("\n PETROBOWL RODADA {}".format(rodada))
    time_vencedor = input("Qual time acertou OU errou? (1/2/0): ") #0 é se nenhum time respondeu.
    if int(time_vencedor) >= (3): #Condição para não crashar o programa caso insina um número inválido.
        print("\n Você inseriu um número não válido. Insira novamente.\n")
        continue #Caso isso aconteça, o programa volta para o primeiro input no loop
                 #e não contabiliza como rodada.
    rodada = rodada + 1 #A partir daqui, soma-se 1 ao número da rodada.

    if time_vencedor == "1":
        pontos_vencedor = int(input("Quantos pontos o time que acertou ganhou ou perdeu (-)? "))
        pts_time1.append(pontos_vencedor) #Adiciona os pontos na lista de toss-up.
    elif time_vencedor == "2":
        pontos_vencedor = int(input("Quantos pontos o time que acertou ganhou ou perdeu (-)? "))
        pts_time2.append(pontos_vencedor)
    elif time_vencedor == "0": #Se nenhum time acertou, mesmo assim deve-se adicionar um valor 0 em alguma
        pontos_vencedor = 0    #das listas, pois assim contabiliza como rodada para interromper o loop.
        pts_time1.append(pontos_vencedor)
        total_1 = sum(pts_time1) + sum(bonus_time1) #Essa parte existe pois mesmo nenhum time tendo acertado,
        total_2 = sum(pts_time2) + sum(bonus_time2) #queremos mostrar o placar.
        print("\n Pontos time 1: {} \n Pontos time 2: {}\n".format(total_1, total_2))
        continue

    bonus = int(input("O time acertou quantos pontos na bônus? "))
    #Agora se insere a quantidade de bônus que o time acertou.
    if (bonus != 0) and time_vencedor == "1":
        bonus_time1.append(bonus)
    elif (bonus != 0) and time_vencedor == "2":
        bonus_time2.append(bonus)
    else:
        total_1 = sum(pts_time1) + sum(bonus_time1)
        total_2 = sum(pts_time2) + sum(bonus_time2)

        print("\n Pontos time 1: {} \n Pontos time 2: {}\n".format(total_1, total_2))
        continue

    total_1 = sum(pts_time1) + sum(bonus_time1)
    total_2 = sum(pts_time2) + sum(bonus_time2)

    print("\n Pontos time 1: {} \n Pontos time 2: {}\n\n".format(total_1, total_2))

    if (len(pts_time1) + len(pts_time2)) == numero_rodadas: #Break quando atingir o número de rodadas.
        break

print("\nFIM DAS RODADAS.\n")

if (total_1 > total_2): #Condições para definir equipe campeã.
    print("Equipe campeã: {}".format("Equipe 1."))
elif (total_1 < total_2):
    print("Equipe campeã: {}".format("Equipe 2."))
elif (total_1 == total_2):
    print("Empate.")

input("\n\n\nPressione enter para fechar...")

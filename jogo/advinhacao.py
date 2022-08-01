import random


def jogo():
    print("**************************")
    print("Começando o jogo")
    print("**************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000



    print("qual nivel da tentativa?")
    print("(1) Facil, (2) Medio, (3) Dificil")

    nivel = int(input("define o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5




    for rodada in range(1,total_de_tentativas + 1) :
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100 ):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        print("Voce digitou ", chute)


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (acertou):
            print("você acertou e fez {} pontos" .format(pontos))
            break

        else:
            if(maior):
                print("o chute foi maior")
            elif(menor):
                print("o chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



    print("obrigado por jogar")





if(__name__ == "__main__"):
    jogo()
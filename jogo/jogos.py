import advinhacao
import forca


def escolha_jogo():
    print("**************************")
    print("******Escolha o jogo******")
    print("**************************")


    print("(1) Forca, (2) Advinhação")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("*Iniciando Forca*")
        forca.jogo()


    elif(jogo == 2):
        print("*Iniciando Advinhação*")
        advinhacao.jogo()


if(__name__ == "__main__"):
    escolha_jogo()
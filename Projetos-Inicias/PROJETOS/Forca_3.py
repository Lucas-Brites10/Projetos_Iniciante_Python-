with open("aa.txt", "r") as arquivo:
    palavras_geradas = arquivo.readlines()

from random import choice as ch
from unidecode import unidecode

palavra = ch(palavras_geradas)

class JogoDaForca():

    def __init__(self):

        print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
        print("           Vamos começar o jogo!")
        print(" Você terá 6 tentativas para acertar a palavra!")
        print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")

    def Iniciar(self):

        a = list(palavra)
        palavra_escolhida = []

        while len(palavra_escolhida) == 0:
            for I in a:
                if I not in "\ufeff, \n":
                    palavra_escolhida.append(I)
                else:
                    break

        for M in range(len(palavra_escolhida)):
            palavra_escolhida[M] = palavra_escolhida[M].upper()
            palavra_escolhida[M] = unidecode(palavra_escolhida[M])



        tentativas = True
        c = 0
        c_ = 0

        palavra_tentativas = ["_"] * len(palavra_escolhida)
        letras_erradas = []

        ganhou = False
        dica = False
        respondeu = False

        gerada = False

        if len(palavra_escolhida) > 0:
            gerada = True

        if palavra_escolhida == []:
            gerada = False
            jogar()  # Se a palavra sorteada bugar e não for nada ([]) o jogo será reiniciado

        elif gerada==True:

            print("\nPALAVRA » ", end="")

            for LE in palavra_tentativas: print(LE, end=" ")

            while tentativas:

                letra_presente = False

                try:

                    cor_b = '\033[33m'
                    print("\n")
                    resposta = input(f"{cor_b}        Digite a letra: ").strip()
                    unidecode(resposta)
                    respondeu = True

                    if len(resposta) > 1:
                        print("\nPor favor, insira apenas uma letra!")
                        c -= 1
                        resposta

                    elif len(resposta) == 0:
                        respondeu = False
                        break

                    resposta = resposta.upper().strip()

                    if resposta in letras_erradas:
                        print(f"\nVocê ja digitou anteriormente a letra {resposta}")
                        c -= 1

                    resposta

                    for I in range(len(palavra_escolhida)):

                        if resposta in palavra_escolhida[I]:
                            palavra_tentativas[I] = palavra_escolhida[I]
                            letra_presente = True

                    if not letra_presente:
                        c += 1
                        cor = '\033[31m'
                        print(f"  Você tem {cor}{6 - c}{cor_b} tentativas restantes!")

                        letras_erradas.append(resposta)

                    for J in palavra_tentativas:
                        if J == "_":
                            print('   \033[35m', J, end="")

                        else:
                            print("   \033[34m", J, end="")


                    if c == 5 and dica == False:

                        dica = input("\n\nDeseja uma dica? (S/N)\n").upper()
                        if dica in "SSIM":
                            qual_letra = int(input(f"\nQual a letra gostaria de descobrir? 0-{len(palavra_escolhida)-1}\n:"))
                            print(palavra_escolhida[qual_letra])
                            dica = True

                        elif dica in "NNÃO":
                            continue

                    if c == 6:
                        print("\n    A palavra era »", end=" ")
                        for I in palavra_escolhida:
                            print(I, end='')
                        break

                except:
                    print("Ocorreu um erro ao rodar o programa!")
                    jogar()

                if "_" in palavra_tentativas:
                    continue
                else:
                    ganhou = True
                    print("\n      Parabéns, você ganhou!")
                    break


jogar = JogoDaForca()
jogar.Iniciar()

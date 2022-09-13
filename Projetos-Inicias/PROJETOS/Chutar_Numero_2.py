from random import randrange

class ChutarNumero():

    #CRIAR UM PROGRAMA QUE GERE UM NÚMERO ALEATORIO DE 1 - 100 ATÉ EU ACERTAR.
    #O PROGRAMA DEVE DAR DICA SE PRECISO CHUTAR UM NÚMERO MAIOR OU MENOR.

    def __init__(self): #Comportamento inicial da função iniciar ↓

        self.valor_aleatorio = None
        self.valor_minimo = 1
        self.valor_maximo = 100

    def Iniciar(self):

        self.gerar_aleatorio()  # GERANDO UM NÚMERO ALEATORIO DE 1-100
        acertou = False


        while not acertou:


            print('\n')
            self.PedirValorAleatorio() # FAZENDO A PERGUNTA DO CHUTE

            "ACERTOU:"
            if self.resposta == self.valor_aleatorio:
                print("Acertou!")
                acertou = True

            else:

                if self.resposta > self.valor_aleatorio:
                    print("Chute um número menor!")
                    continue


                elif self.resposta < self.valor_aleatorio:
                    print("Chute um número maior!")
                    continue


    def PedirValorAleatorio(self):
        self.resposta = int(input(f"Chute um número de {self.valor_minimo} - {self.valor_maximo} » "))


    def gerar_aleatorio(self):
        self.valor_aleatorio = randrange(self.valor_minimo, self.valor_maximo)


jogar = ChutarNumero()

jogar.Iniciar()


"""https://www.youtube.com/watch?v=7U3-pJZkN-o&ab_channel=DevAprender 49minutos"""
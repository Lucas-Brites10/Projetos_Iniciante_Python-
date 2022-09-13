import random
import PySimpleGUI as sg


class JogarDados:

    def __init__(self): #Comportamento inicial da def abaixo:
        self.valor_minimo = 1
        self.valor_maximo = 6
        #LAYOUT:
        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

    def jogar(self):
        #CRIAR UMA JANELA:
        self.janela = sg.Window("Simulador de Dado", layout=self.layout)
        #LER VALORES DA TELA:
        self.eventos, self.valores = self.janela.Read()

        #INTERAGIR COM OS VALORES:

        try:

            if self.eventos == "Sim" or self.eventos == "s":
                self.GerarValorDado()
            elif self.eventos == "Não" or self.eventos == "n":
                print("Agradecemos sua utilização do programa!")
            else:
                print("Não entendi sua resposta tente novamente!")

        except:

            print("Ocorreu um erro ao captar sua resposta.")

    def GerarValorDado(self):
        jogada = random.randrange(self.valor_minimo, self.valor_maximo)
        print(f"\nO valor do dado jogado foi » \033[31m{jogada}")


simulador = JogarDados()
simulador.jogar()
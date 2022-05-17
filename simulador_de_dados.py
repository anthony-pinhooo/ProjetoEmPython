import random

class SimuladorDado:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = "Você gostaria de girar o dado novamente ?\n"
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
                
            elif resposta == 'não' or resposta == 'nao' or resposta == 'n':
                print("Ok ! Obrigado por participar !")     
                
            else:
                print("Favor, digitar sim ou não")
                
        except:
            print("Erro ! Ocorreu um erro ao receber sua resposta")
            
    def GerarValorDoDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))
        
        
simulador = SimuladorDado()
simulador.Iniciar()
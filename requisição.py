#Importando biblioteca com função de limpeza

import os

# Definindo a classe 

class Manobra:
#Chamando o modo construtor __init__
    def __init__(self, solicitante:str, letra:str, data_solicitada:str, data_executar:str, hora_solicitada:str):
        self.solicitante = solicitante
        self.letra = letra
        self.data_solicitada = data_solicitada
        self.hora_solicitada = hora_solicitada
        self.data_executar = data_executar
        
#Criando o método dados        
    def dados(self):
        print(f'Solicitante: {self.solicitante}\nLetra: {self.letra}\nData de Solicitação: {self.data_solicitada}\nHora Solicitada {self.hora_solicitada}\nData para Execução: {self.data_executar}\n')

#Criando o método bobina
    def bobina(self, nome:str):
        print(f'Bobina: {nome}')
    
#Criando o método local
    def local(self, de:str, para:str):
        print(f'Origem: {de}\nDestino: {para}')

def limpar():
  os.system('clear')  

#Colhendo informações para instanciar a classe Manobra
print("REQUISIÇÃO DE MANOBRA DE JUMBO V1.0\n")

solicitante=input("Solicitante: ")
letra=input("Letra: ")
data_solicitada=input("Data de Solicitação: ")
hora_solicitada=input("Hora de Solicitação: ")
data_executar=input("Data para executar: ")
limpar()

print("REQUISIÇÃO DE MANOBRA DE JUMBO V1.0\n")
print("   Informações sobre Bobina/Local\n")
nome=input("Bobina: ")
de=input('Origem: ')
para=input('Destino: ' )
limpar()

print("REQUISIÇÃO DE MANOBRA DE JUMBO V1.0\n")
print("         RESULTADO DAS INFORMAÇÕES COLETADAS\n")
#Chamando os métodos para execução
manobra = Manobra(solicitante=(solicitante), letra=(letra), data_solicitada=(data_solicitada), hora_solicitada=(hora_solicitada), data_executar=(data_executar))
manobra.dados()
manobra.bobina(nome=(nome))
manobra.local(de=(de),para=(para))

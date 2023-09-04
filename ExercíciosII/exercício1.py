# 1) Crie uma classe que modele o objeto "carro"
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo 
        self.ligado = False
        self.velocidade = 0.0
        self.limite_velocidade = 110.0

#Um carro tem que ter os seguintes comportamentos: liga, desliga, acelera, desacelera.

    def liga(self):
       self.ligado = True
    
    def desliga(self):
       self.ligado = True
       self.velocidade = 0.0

    def acelera(self):
       if self.ligado == False:
        return
       
       if self.velocidade < self.limite_velocidade:
          self.velocidade += 5
    
    def desacelera(self):
       if self.ligado == False:
        return
       
       if self.velocidade > 0:
          self.velocidade = self.velocidade - 5
    
    def __str__(self):
       ligado_str = "ligado" if self.ligado == True else "desligado"
       
       return f"Carro {self.modelo} da cor {self.cor} está {ligado_str}, à velocidade de {self.velocidade} km/h"
  
# Crie uma instância da classe carro.
carro = Carro("vermelha", "Uno Vivace")
print(carro)

#Faça o carro "andar" utilizando os métodos da sua classe.
carro.liga()
print(carro)

for i in range(5):
  carro.acelera()
print(carro)

#Faça o carro "parar" utilizando os métodos da sua classe.
carro.desliga()
print(carro)
from oo.motor import Motor
from oo.direcao import Direcao

class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.valor

if __name__ == '__main__':
    direcao = Direcao()
    motor = Motor()
    carro = Carro(motor,direcao)
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    print(carro.calcular_direcao())
    carro.girar_a_direita()
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())

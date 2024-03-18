from turtle import Turtle

class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.nota_esquerda = 0
        self.nota_direita = 0
        self.updade_placar()

    def updade_placar(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.nota_esquerda, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.nota_direita, align="center", font=("courier", 80, "normal"))

    def ponto_esquerdo(self):
        self.nota_esquerda += 1
        self.updade_placar()

    def ponto_direito(self):
        self.nota_direita += 1
        self.updade_placar()

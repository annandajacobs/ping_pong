from turtle import Screen, Turtle
from taco import Taco
from bola import Bola
from placar import Placar
import time

#configurando tela
tela = Screen()
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.title("Pong")
tela.tracer(0)  #controla as animaçoes

taco_direito = Taco((350, 0))
taco_esquerdo = Taco((-350, 0))
bola = Bola()
placar = Placar()

tela.listen()
tela.onkey(taco_direito.go_up, "Up")
tela.onkey(taco_direito.go_down, "Down")
tela.onkey(taco_esquerdo.go_up, "w")
tela.onkey(taco_esquerdo.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(bola.velocidade)
    tela.update()
    bola.move() 

    #detectar colisão com a parede
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.quicar_y()

    #detectar colisão com os tacos
    if bola.distance(taco_direito) < 50 and bola.xcor() > 320 or bola.distance(taco_esquerdo) < 50 and bola.xcor() < -320:
        bola.quicar_x()

    #detectar falha do taco direito
    if bola.xcor() > 380:
        bola.reiniciar()
        placar.ponto_esquerdo()

    #detectar falha do taco esquerdo
    if bola.xcor() < -380:
        bola.reiniciar()
        placar.ponto_direito()

tela.exitonclick()
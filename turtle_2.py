#Labirinto

from turtle import *

shape('turtle')

reta = int(10)
velocidade = int(5)

for i in range(1000):
    Turtle()
    speed(velocidade)

    forward(reta)
    right(90)

    reta+=10
    velocidade+=1

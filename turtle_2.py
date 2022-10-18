#Labirinto

from turtle import *

shape('turtle')

reta = 10
velocidade = 5

for i in range(1000):
    Turtle().pencolor('white')
    speed(velocidade)

    forward(reta)
    right(90)

    reta+=10
    velocidade+=10**3

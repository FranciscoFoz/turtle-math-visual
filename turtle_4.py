#Concha

from turtle import *


shape('turtle')
speed(10)

def quadrado(comprimento_aresta):
    for i in range(4):
        forward(comprimento_aresta)
        right(90)

comprimento_aresta = 100

for i in range(70):   
    quadrado(comprimento_aresta)
    right(5)
    comprimento_aresta+=5

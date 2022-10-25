#Flor

from turtle import *

shape('turtle')
speed(10)

comprimento_aresta = 100

def triangulo(comprimento_aresta):
    for i in range(3):
        forward(comprimento_aresta)
        right(120)

for i in range(15):
    for circulo_1 in range(2):
        triangulo(comprimento_aresta)
        right(5)
    for circulo_2 in range(2):
        triangulo(comprimento_aresta + 50)
        right(5)
    for circulo_3 in range(2):
        triangulo(comprimento_aresta + 100)
        right(5)

done()
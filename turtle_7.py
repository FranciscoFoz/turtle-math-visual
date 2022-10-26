#Circulo das estrelas

from turtle import *

shape('turtle')
speed(10)

comprimento_aresta = 10

def estrela(comprimento_aresta):
    for i in range(5):
        forward(comprimento_aresta)
        right(144)

for i in range(60):
    estrela(comprimento_aresta)
    right(5)
    comprimento_aresta+=10

done()
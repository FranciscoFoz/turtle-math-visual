#Polígono

from turtle import *

shape('turtle')
speed(10)

quantidade_lados = int(input("Insira a quantidade de números do polígono : "))

comprimento_aresta = int(input("Insira o comprimento de cada aresta do polígono : "))

def poligono():
    for i in range(quantidade_lados):
        forward(comprimento_aresta)
        right(360 / quantidade_lados)


poligono()

done()
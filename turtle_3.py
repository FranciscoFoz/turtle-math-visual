#Mandala 

from turtle import *

shape('turtle')
speed(10)

def quadrado(comprimento_aresta):
    for i in range(4):
        forward(comprimento_aresta)
        right(90)

for i in range(185):   
    quadrado(100)
    right(2) 

for i in range(83):  
    quadrado(100)
    right(5)
    quadrado(125)
    right(5)
    quadrado(150)
    right(5)    
    quadrado(175)
    right(5)
    quadrado(200)
    right(5)
    quadrado(225)
    right(5)
    quadrado(250)
    right(5)





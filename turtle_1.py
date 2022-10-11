#Começando com turtle

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('blue')

a = 0
b = 0

t.speed(1000)
t.goto(-220,210)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a+=1
    b+=1
    if b==2000:
        break
    
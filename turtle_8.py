#Incompleto...

from math import sqrt


def plug():
    x = -100 
    while x < 100: 
        if 2*x + 5 == 13: 
            print("x =",x) 
        x += 1


def quad(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

    return print(x1,x2)




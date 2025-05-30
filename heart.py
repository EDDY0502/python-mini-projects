import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (12 * math.cos(k)
            - 5 * math.cos(2 * k)
            - 2 * math.cos(3 * k)
            - math.cos(4 * k))

speed(0)              # Fastest drawing speed
bgcolor("black")      
color("#f73487")      # Set color once
penup()               # Start with pen up

for i in range(6000):
    k = i * 0.01      # Fine resolution for smooth curve
    x = hearta(k) * 20
    y = heartb(k) * 20
    goto(x, y)
    pendown()

hideturtle()
done()

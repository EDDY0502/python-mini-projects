import math
from turtle import *
def hearta(k): #k is the angle in radians.
    return 15*math.sin(k)**3 #15 * sin(k) is part of a parametric heart equation.
def heartb(k):
    return (12 * math.cos(k) #The base wave pattern (largest component of the shape)
            - 5 * math.cos(2 * k) #Adds "dips" or curves to refine the heart shape
            - 2 * math.cos(3 * k) #Adds more detail to the top dip and bottom point
            - math.cos(4 * k)) #Further refines the sharpness of curves and symmetry
    
speed (0)
bgcolor("black")
for i in range(6000): #Loops 6000 times
    goto(hearta(i)*20,heartb(i)*20) #Moves the turtle to the heart coordinates,Multiplies by 20 to scale up the shape.
    for j in range (5): #Repeats 5 times, but just sets the color again and again.
        color("#f73487")
    goto(0,0)
done()

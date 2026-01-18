from turtle import Turtle
# Turtle → CLASS (from turtle module)

import random
# random module → used for abstraction of randomness


class Food(Turtle):
    # Food → CLASS (user-defined)
    # Inheritance: Food class INHERITS from Turtle class
    # This means Food gets all methods and attributes of Turtle

    def __init__(self):
        # __init__() → CONSTRUCTOR METHOD
        # Called automatically when a Food OBJECT is created
        
        super().__init__()
        # super() → calls the constructor of the parent class (Turtle)
        # Enables inheritance functionality
        
        self.shape("circle")
        # shape() → METHOD (inherited from Turtle)
        # Attribute: shape of food object
        
        self.penup()
        # penup() → METHOD
        # Attribute: pen state (no drawing while moving)
        
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # shapesize() → METHOD
        # Attribute: size of the food
        
        self.color("blue")
        # color() → METHOD
        # Attribute: color of the food
        
        self.speed("fastest")
        # speed() → METHOD
        # Attribute: movement speed
        
        self.refresh()
        # refresh() → METHOD (defined below)
        # Abstraction: hides food positioning logic


    def refresh(self):
        # refresh() → METHOD
        # Abstraction: handles food relocation logic
        
        random_x = random.randint(-289, 288)
        # randint() → METHOD
        # Generates random x-coordinate
        
        random_y = random.randint(-288, 288)
        # Generates random y-coordinate
        
        self.goto(random_x, random_y)
        # goto() → METHOD (inherited from Turtle)
        # Attribute: position of food object updated

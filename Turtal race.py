from turtle import Turtle, Screen
# Turtle and Screen → CLASSES (blueprints provided by turtle module)

import random
# random module → used for abstraction of randomness


is_race_on = False
# Normal variable (controls program flow, not OOP)


screen = Screen()
# Screen → CLASS
# screen → OBJECT created from Screen class

screen.setup(width=500, height=400)
# setup() → METHOD
# Encapsulation: screen size handling is hidden inside Screen class


user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)
# textinput() → METHOD
# Abstraction: hides GUI input handling


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# LIST → stores multiple color values

y_positions = [-70, -40, -10, 20, 50, 80]
# LIST → stores y-coordinates for turtle placement

all_turtles = []
# LIST → will store Turtle OBJECTS


# ---------------- CREATE MULTIPLE OBJECTS ----------------
for turtle_index in range(0, 6):
    # Loop → used to create multiple objects (reusability)
    
    new_turtle = Turtle(shape="turtle")
    # Turtle → CLASS
    # new_turtle → OBJECT (each loop creates a new object)
    
    new_turtle.penup()
    # penup() → METHOD
    # Attribute: pen state changed (no drawing)
    
    new_turtle.color(colors[turtle_index])
    # color() → METHOD
    # Attribute: turtle color
    
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # goto() → METHOD
    # Attributes: x and y position of turtle
    
    all_turtles.append(new_turtle)
    # Storing OBJECTS inside a list (object collection)


if user_bet:
    # Checks if user entered a bet
    is_race_on = True
    # Starts the race


# ---------------- RACE LOGIC ----------------
while is_race_on:
    # Loop keeps race running
    
    for turtle in all_turtles:
        # turtle → OBJECT taken from list of Turtle objects
        
        if turtle.xcor() > 230:
            # xcor() → METHOD
            # Attribute: current x-coordinate of turtle
            
            is_race_on = False
            # Stops the race
            
            winning_color = turtle.pencolor()
            # pencolor() → METHOD
            # Attribute: color of the winning turtle
            
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        # randint() → METHOD
        # Abstraction: random movement logic hidden
        
        turtle.forward(rand_distance)
        # forward() → METHOD
        # Moves turtle using its internal state


screen.exitonclick()
# exitonclick() → METHOD
# Encapsulation: event handling hidden inside Screen class

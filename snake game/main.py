from turtle import Screen
# Screen → CLASS (provided by turtle module)

from snake import Snake
# Snake → CLASS (user-defined, blueprint for snake behavior)

from food import Food
# Food → CLASS (user-defined, blueprint for food object)

from scoore_board import Scooreboard
# Scooreboard → CLASS (user-defined, blueprint for score handling)

import time
# time module → used for abstraction of delay


screen = Screen()
# screen → OBJECT created from Screen class

screen.setup(width=600, height=600)
# setup() → METHOD
# Encapsulation: screen size handling hidden inside Screen class

screen.bgcolor("black")
# bgcolor() → METHOD
# Attribute: background color of screen

screen.title("My Snake Game")
# title() → METHOD
# Attribute: title of the game window

screen.tracer(0)
# tracer() → METHOD
# Encapsulation: controls screen refresh internally


snake = Snake()
# Snake → CLASS
# snake → OBJECT created from Snake class

food = Food()
# Food → CLASS
# food → OBJECT created from Food class

scooreboard = Scooreboard()
# Scooreboard → CLASS
# scooreboard → OBJECT created from Scooreboard class


screen.listen()
# listen() → METHOD
# Abstraction: listens for keyboard input


screen.onkey(snake.up, "Up")
# onkey() → METHOD
# snake.up → METHOD of Snake class (movement behavior)

screen.onkey(snake.down, "Down")
# down() → METHOD of Snake class

screen.onkey(snake.left, "Left")
# left() → METHOD of Snake class

screen.onkey(snake.right, "Right")
# right() → METHOD of Snake class


game_is_on = True
# Normal variable controlling game loop (not OOP)


while game_is_on:
    # Main game loop
    
    screen.update()
    # update() → METHOD
    # Encapsulation: redraws screen internally
    
    time.sleep(0.1)
    # sleep() → METHOD
    # Abstraction: pauses execution
    
    snake.move()
    # move() → METHOD of Snake class
    # Updates snake position using internal attributes
    
    
    # -------- EATING FOOD (OBJECT INTERACTION) --------
    if snake.head.distance(food) < 15:
        # head → ATTRIBUTE of snake object
        # distance() → METHOD
        # Object-to-object interaction
        
        food.refresh()
        # refresh() → METHOD of Food class
        
        snake.extend()
        # extend() → METHOD of Snake class
        # Adds new segment (object modification)
        
        scooreboard.increase_score()
        # increase_score() → METHOD
        # Attribute: score updated
    
    
    # -------- WALL COLLISION --------
    if (
        snake.head.xcor() > 280 or
        snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or
        snake.head.ycor() < -280
    ):
        # xcor(), ycor() → METHODS
        # Attributes: position of snake head
        
        game_is_on = False
        # Stops the game
        
        scooreboard.game_over()
        # game_over() → METHOD
        # Displays game over message
    
    
    # -------- SELF COLLISION --------
    for segment in snake.segments[1:]:
        # segments → ATTRIBUTE (list of snake body parts)
        # segment → OBJECT inside the list
        
        if snake.head.distance(segment) < 10:
            # distance() → METHOD
            # Object-to-object interaction
            
            game_is_on = False
            # Stops the game
            
            scooreboard.game_over()
            # game_over() → METHOD


screen.exitonclick()
# exitonclick() → METHOD
# Encapsulation: handles screen closing event

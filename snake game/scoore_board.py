from turtle import Turtle
# Turtle → CLASS (from turtle module)


class Scooreboard(Turtle):
    # Scooreboard → CLASS (user-defined)
    # Inheritance: Scooreboard INHERITS from Turtle class
    # Means Scooreboard gets all Turtle methods and attributes

    def __init__(self):
        # __init__() → CONSTRUCTOR METHOD
        # Runs automatically when a Scooreboard OBJECT is created
        
        super().__init__()
        # super() → calls parent class (Turtle) constructor
        # Enables inheritance
        
        self.score = 0
        # score → ATTRIBUTE
        # Stores current score value
        
        self.color("white")
        # color() → METHOD (inherited)
        # Attribute: text color
        
        self.penup()
        # penup() → METHOD
        # Attribute: pen state (no drawing lines)
        
        self.goto(0, 270)
        # goto() → METHOD
        # Attribute: position of scoreboard
        
        self.update_scooreboard()
        # update_scooreboard() → METHOD
        # Abstraction: hides score display logic
        
        self.hideturtle()
        # hideturtle() → METHOD
        # Encapsulation: hides turtle cursor


    def update_scooreboard(self):
        # update_scooreboard() → METHOD
        # Abstraction: handles how score is displayed
        
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Courier", 15, "normal")
        )
        # write() → METHOD
        # Uses score ATTRIBUTE to display text


    def game_over(self):
        # game_over() → METHOD
        # Abstraction: handles game over display
        
        self.goto(0, 0)
        # Move turtle to screen center
        
        self.write(
            "GAME OVER",
            align="center",
            font=("Courier", 15, "normal")
        )
        # Displays game over message


    def increase_score(self):
        # increase_score() → METHOD
        # Abstraction: handles score update logic
        
        self.score += 1
        # Modifies score ATTRIBUTE
        
        self.clear()
        # clear() → METHOD
        # Clears previous score text
        
        self.update_scooreboard()
        # Updates score display

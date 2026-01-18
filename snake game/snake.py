from turtle import Turtle
# Turtle → CLASS (from turtle module)


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# CONSTANT → stores starting positions for snake body segments

MOVE_DISTANCE = 20
# CONSTANT → distance snake moves each step

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# CONSTANTS → directions in degrees


class Snake:
    # Snake → CLASS (user-defined)
    # Represents the snake in the game
    
    def __init__(self):
        # __init__() → CONSTRUCTOR METHOD
        # Automatically called when a Snake OBJECT is created
        
        self.segments = []
        # segments → ATTRIBUTE
        # Stores Turtle objects representing snake body
        
        self.create_snake()
        # create_snake() → METHOD
        # Abstraction: hides snake creation logic
        
        self.head = self.segments[0]
        # head → ATTRIBUTE
        # Reference to first segment (snake head)
    

    def create_snake(self):
        # create_snake() → METHOD
        # Abstraction: creates initial snake body
        
        for position in STARTING_POSITION:
            self.add_segment(position)
            # Reusability: add_segment() reused
    

    def add_segment(self, position):
        # add_segment() → METHOD
        # Abstraction: handles creation of one snake segment
        
        new_segment = Turtle("square")
        # Turtle → CLASS
        # new_segment → OBJECT created from Turtle class
        
        new_segment.color("white")
        # color() → METHOD
        # Attribute: segment color
        
        new_segment.penup()
        # penup() → METHOD
        # Attribute: pen state
        
        new_segment.goto(position)
        # goto() → METHOD
        # Attribute: segment position
        
        self.segments.append(new_segment)
        # Adds segment OBJECT to segments list
    

    def extend(self):
        # extend() → METHOD
        # Abstraction: adds a new segment to the snake
        
        self.add_segment(self.segments[-1].position())
        # Uses last segment's position (ATTRIBUTE)
    

    def move(self):
        # move() → METHOD
        # Abstraction: moves the snake forward
        
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Loop from last segment to second segment
            
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # xcor(), ycor() → METHODS
            # Attributes: previous segment position
            
            self.segments[seg_num].goto(new_x, new_y)
            # goto() → METHOD
            # Moves current segment
        
        self.head.forward(MOVE_DISTANCE)
        # forward() → METHOD
        # Moves snake head forward
    

    def up(self):
        # up() → METHOD
        # Abstraction: changes direction upward
        
        if self.head.heading() != DOWN:
            # Prevents snake from reversing
            
            self.head.setheading(UP)
            # setheading() → METHOD
    

    def down(self):
        # down() → METHOD
        
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    

    def left(self):
        # left() → METHOD
        
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

    def right(self):
        # right() → METHOD
        
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

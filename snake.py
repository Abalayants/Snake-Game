from turtle import Turtle

"""Constant for starting position with snake body length of 3"""
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
"""Constant for standard move distance which is the size of the turtle"""
MOVE_DISTANCE = 20
"""Constants for directions that the snake is able to move"""
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Class for the snake object
    Creates a snake with a length of 3 and assigns the HEAD which will be the one to choose directions
    When head moves, the body will follow in the exact coordinates the head has gone
    Ability to add segments as more dots are eaten
    Allows for movement of snake without going back on itself
    """

    def __init__(self):
        """List for initial snake with 3 instances of turtle (squares)"""
        self.segments = []
        self.create_snake()  # From method below
        self.head = self.segments[0]  # Assign head turtle

    def create_snake(self):
        """Cycles through the three positions and deposits a turtle into each one"""
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position: tuple):
        """
        Create turtle object from Turtle class
        Make the snake color white for black background
        Initial starting position for the new snake must be set using the arg
        Starter snake size = 3 turtle instances
        """
        starter_turtle = Turtle(shape="square")
        starter_turtle.penup()
        starter_turtle.color("white")
        starter_turtle.goto(position)
        self.segments.append(starter_turtle)

    def reset(self):
        """Move old snake off screen, clear the segments list, create new snake"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Extending the snake by one using the last position in the snake to add another segment"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Using range with start, stop, step to create a way for follower segments to keep up with head of snake
        The 2nd and 3rd segments are in -1, and -2 positions following the head
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Creating coordinates for 2nd and 3rd turtle to follow the first
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Actual follow action for "The Head"
            self.segments[seg_num].goto(new_x, new_y)
        # Movement forward using the size of the snake head as the distance
        self.head.forward(MOVE_DISTANCE)

    """All the ways a snake can move, with checks to prevent it from going back on itself"""
    def up(self):
        self.head.setheading(UP) if self.head.heading() != DOWN else None

    def down(self):
        self.head.setheading(DOWN) if self.head.heading() != UP else None

    def right(self):
        self.head.setheading(RIGHT) if self.head.heading() != LEFT else None

    def left(self):
        self.head.setheading(LEFT) if self.head.heading() != RIGHT else None


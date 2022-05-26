from turtle import Turtle

# sets the coordinates for the default three part body of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# creates a class (blueprint) for a snake object that we will use in the main file
class Snake:

    # initializes the methods that will be used below
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # makes a white square turtle with its pen up for each coordinate in the constant at the top of the file
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # creates a loop so that the last body part of the snake will follow the second to last and so on until the head
    # as well as making the head move forwards 20 pixels
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self,):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

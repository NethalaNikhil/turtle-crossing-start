from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.right(270)
        self.goto(x=0, y=-280)

    def Up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def go_to(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

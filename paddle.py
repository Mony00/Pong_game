from turtle import Turtle
MOVE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

    def down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)


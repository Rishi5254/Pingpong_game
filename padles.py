from turtle import Turtle


class Paddle1(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(-90)

    def down(self):
        self.forward(20)

    def up(self):
        self.backward(20)


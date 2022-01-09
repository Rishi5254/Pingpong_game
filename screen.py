from turtle import Turtle

class StartingScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.middleline()

    def middleline(self):
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.shapesize(1, 0.1)
        self.speed(0)
        self.goto(0,400)
        self.setheading(-90)
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)



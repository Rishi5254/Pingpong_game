from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10


    def ball_move(self):
        x_dir = self.xcor() + self.x_cor
        y_dir = self.ycor() + self.y_cor
        self.goto(x_dir, y_dir)

    def bounce(self):
        self.y_cor *= -1

    def paddel_bounce(self):
        self.x_cor *= -1


    def restart(self):
        self.goto(0, 0)
        self.x_cor *= -1
        self.ball_move()

    def restart_left(self):
        self.goto(0, 0)
        self.x_cor *= -1
        self.ball_move()



from turtle import Turtle

class Score():
    def __init__(self):
        self.scoreofplayer1 = 0
        self.scoreofplayer2 = 0
        self.score1 = Turtle()
        self.score2 = Turtle()

    def player1score(self):
        self.score1.clear()
        self.score1.color("white")
        self.score1.hideturtle()
        self.score1.penup()
        self.score1.goto(-70, 220)
        self.score1.write(arg=f"{self.scoreofplayer1}", font=('Comic Sans', 50 , 'normal'))
        self.scoreofplayer1 += 1


    def player2score(self):

        self.score2.color("white")
        self.score2.hideturtle()
        self.score2.penup()
        self.score2.goto(40, 220)
        self.score2.clear()
        self.score2.write(arg=f"{self.scoreofplayer2}", font=('Comic Sans', 50 , 'normal'))
        self.scoreofplayer2 += 1

from screen import StartingScreen
from turtle import Screen
from padles import Paddle1
from ball import Ball
import time
from score import Score




my_screen = Screen()
my_screen.title("pong")
my_screen.setup(800,600)
my_screen.bgcolor("black")


my_screen.tracer(0)
line = StartingScreen()
paddle = Paddle1((350, 0))
paddle_2 = Paddle1((-350, 0))
ball = Ball()
scoreboard = Score()
scoreboard.player1score()
scoreboard.player2score()



my_screen.listen()
my_screen.onkeypress(paddle.up, "Up")
my_screen.onkeypress(paddle.down, "Down")
my_screen.onkeypress(paddle_2.up, "w")
my_screen.onkeypress(paddle_2.down, "s")


is_on = True
while is_on:
    speed = [(0.09), (0.08), (0.07), (0.06) ]
    time.sleep(0.06)
    my_screen.update()
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if paddle.distance(ball) < 50 and ball.xcor() > 320 or paddle_2.distance(ball) < 50 and ball.xcor() < -320:
        ball.paddel_bounce()


    if ball.xcor() > 380:
        ball.restart()
        scoreboard.player1score()


    elif ball.xcor() < -380:
        ball.restart_left()
        scoreboard.player2score()




my_screen.exitonclick()



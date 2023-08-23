from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # turns off animation on the screen

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()  # refresh screen

screen.exitonclick()

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.start_pos = start_pos
        self._create_paddle()

    def _create_paddle(self):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.start_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

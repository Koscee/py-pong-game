from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        score_font = ("Courier", 40, "bold")
        text_align = "center"
        y_pos = 240
        self.clear()
        self.goto(-100, y_pos)
        self.write(self.left_score, align=text_align, font=score_font)
        self.goto(100, y_pos)
        self.write(self.right_score, align=text_align, font=score_font)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

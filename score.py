from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.sety(279)
        self.color("white")
        self.scoree = 0
        self.scoreee = 0
        self.write(arg=f"{self.scoreee}   SCORE   {self.scoree}", align="center", font=("Arial", 15, "normal"))

    def score(self):
        self.scoree = self.scoree + 1
        self.clear()
        self.write(arg=f"{self.scoreee}   SCORE   {self.scoree}", align="center", font=("Arial", 15, "normal"))

    def score1(self):
        self.scoreee = self.scoreee + 1
        self.clear()
        self.write(arg=f"{self.scoreee}   SCORE   {self.scoree}", align="center", font=("Arial", 15, "normal"))

    def over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"{self.scoreee}   SCORE   {self.scoree}", align="center", font=("Arial", 15, "normal"))
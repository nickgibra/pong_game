from turtle import Turtle
class Cosodestra:
    def __init__(self, coor):
        self.coo = coor
        self.create()

    def create(self):
        self.body = Turtle(shape="square")
        self.body.shapesize(5, 1)
        self.body.penup()
        self.body.color("white")
        self.body.setx(self.coo)

    def up(self):
        y = self.body.ycor() + 20
        self.body.goto(self.body.xcor(), y)
    def down(self):
        y = self.body.ycor() - 20
        self.body.goto(self.body.xcor(), y)
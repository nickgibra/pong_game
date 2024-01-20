from turtle import Turtle
import random


class Palla:
    def __init__(self):
        self.create()
        self.speed = 5

    def create(self):
        self.body = Turtle(shape="circle")
        self.body.penup()
        self.body.color("white")
        if random.randint(0,1) == 0:
            if random.randint(0, 1) == 0:
                self.body.setheading(random.randint(136, 179))
            else:
                self.body.setheading(random.randint(181, 224))
        else:
            if random.randint(0, 1) == 0:
                self.body.setheading(random.randint(316, 359))
            else:
                self.body.setheading(random.randint(361, 404))



    def move(self):
        self.body.forward(self.speed)
        if self.body.ycor() >= 290 or self.body.ycor() <= -280:
            self.body.setheading(360 - self.body.heading())

    def rimbalzo(self):
        self.body.setheading(180 - self.body.heading())
        self.speed = self.speed + 1


    def refresh(self, n):
        self.speed = 5
        self.body.setx(0)
        self.body.sety(0)
        if n == 0:
            if random.randint(0, 1) == 0:
                self.body.setheading(random.randint(136, 179))
            else:
                self.body.setheading(random.randint(181, 224))
        else:
            if random.randint(0, 1) == 0:
                self.body.setheading(random.randint(316, 359))
            else:
                self.body.setheading(random.randint(361, 404))
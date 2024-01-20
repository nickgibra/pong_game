from turtle import Screen
from cosodestra import Cosodestra
from palla import Palla
import time
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

destra = Cosodestra(350)
sinistra = Cosodestra(-350)
palla = Palla()
scoree = Score()
pc = screen.textinput("VS IA?", "si/no o duo")

screen.listen()
screen.onkey(destra.up, "Up")
screen.onkey(destra.down, "Down")

while True:
    palla.move()
    screen.update()
    time.sleep(0.01)
    if palla.body.distance(sinistra.body) < 60 and palla.body.xcor() <= -330:
        palla.rimbalzo()

    if palla.body.distance(destra.body) < 60 and palla.body.xcor() >= 330:
        palla.rimbalzo()

    if  palla.body.xcor() > 380 or palla.body.xcor() < -380:
        if palla.body.xcor() > 380:
            scoree.score1()
            palla.refresh(0)
        else:
            palla.refresh(1)
            scoree.score()
    if scoree.scoree == 5 or scoree.scoreee == 5:
        scoree.over()
        break
    if pc == "no":
        screen.onkey(sinistra.up, "w")
        screen.onkey(sinistra.down, "s")
    else:
        if palla.body.ycor() > sinistra.body.ycor():
            sinistra.up()
        elif palla.body.ycor() < sinistra.body.ycor():
            sinistra.down()
        if pc == "duo":
            if palla.body.ycor() > destra.body.ycor():
                destra.up()
            elif palla.body.ycor() < destra.body.ycor():
                destra.down()




screen.exitonclick()
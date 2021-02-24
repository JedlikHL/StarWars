import turtle
import random
import time


def fel():
    ypozicio=urhajo.ycor()
    ypozicio+=10
    urhajo.sety(ypozicio)

def le():
    ypozicio=urhajo.ycor()
    ypozicio-=10
    urhajo.sety(ypozicio)

def jobbra():
    xpozicio=urhajo.xcor()
    xpozicio+=10
    urhajo.setx(xpozicio)

def balra():
    xpozicio=urhajo.xcor()
    xpozicio-=10
    urhajo.setx(xpozicio)


space = turtle.Screen()
space.addshape("sprite.gif")
space.tracer(0)
space.setup(width=800, height=600)
space.bgpic("hatter.png")
space.listen()
space.onkey(balra,"Left")
space.onkey(jobbra,"Right")
space.onkey(fel,"Up")
space.onkey(le,"Down")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")

while True:

    space.update()
    time.sleep(0.2)

    if urhajo.ycor() > 300:
        urhajo.sety(-300)
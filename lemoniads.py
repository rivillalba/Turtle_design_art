#exploring color mode
import turtle
turtle.colormode(255)
bob = turtle.Turtle()
todd = turtle.Turtle()
bob.speed(11)
todd.speed(11)
bob.shape("triangle")
todd.shape("square")
from functions import*
turtle.bgcolor(0,0,0)

meh(todd,bob)
bob.penup()
bob.goto(0,0)
bob.pendown()
meh2(todd,bob)

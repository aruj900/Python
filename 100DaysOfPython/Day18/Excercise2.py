from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(50):
    timmy.forward(10)
    timmy.pu()
    timmy.forward(10)
    timmy.pd()

screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen

timmy = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape in range(3,10):
    draw_shape(shape)
screen = Screen()
screen.exitonclick()
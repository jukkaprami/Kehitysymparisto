import turtle
from itertools import cycle

corlors = cycle(['#FF0000', 'orange', 'yellow', \
                 'green', 'blue', 'purple', '#FF00FF', '#00FF00'])

def draw_circle(size, angle, shift):
    turtle.pencolor(next(corlors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(10)
draw_circle(30, 45, 10)
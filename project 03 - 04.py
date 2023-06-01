import turtle

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_square(size, angle, shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
        
    turtle.right(angle)
    turtle.forward(shift)
    draw_square(size+5, angle+1, shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(5)
draw_square(30, 0, 1)

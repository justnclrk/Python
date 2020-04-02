# Try drawing a simple picture using the Python module Turtle.

import turtle
raphael = turtle.Turtle()
raphael.color('black', '#008616')
raphael.speed(10)
raphael.pensize(8)
# head
raphael.begin_fill()
while True:
    raphael.forward(1)
    raphael.left(1.15)
    if abs(raphael.pos()) < 1:
        break
raphael.end_fill()

raphael.penup()
raphael.forward(50)
raphael.pendown()

# shell
raphael.color('black', '#684A03')
raphael.begin_fill()
for i in range(313):
    raphael.forward(2)
    raphael.left(1.15)
raphael.end_fill()

turtle.done()

__author__ = 'Matthew'

# your code here
__author__ = 'Matthew'

import turtle
wn = turtle.Screen()
wn.bgcolor("white")

app = turtle.Turtle()
app.color("black"),app.shape("arrow")

app2 = turtle.Turtle()
app2.color("black"),app2.shape("arrow")

def odd():
    app.pendown()
    app2.pendown()
    for size in range(2):
        app.right(-45), app.forward(60),app.right(-90),app.forward(60),app.left(-135)

    for size in range(2):
        app2.right(-135),app2.forward(60),app2.right(90),app2.forward(60),app2.left(-45)

    app.penup(),app.goto(0,0)
    app2.penup(),app2.goto(0,0)

def main():
    for i in range(4):
        odd()
        app.right(90)
        app2.right(90)
main()

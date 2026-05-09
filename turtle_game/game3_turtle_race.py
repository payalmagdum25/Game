import turtle
import random

def start_game():
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.bgcolor("lightyellow")

    t1 = turtle.Turtle()
    t2 = turtle.Turtle()

    t1.color("red")
    t2.color("blue")

    t1.penup()
    t2.penup()

    t1.goto(-280, 50)
    t2.goto(-280, -50)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 200)

    while True:
        t1.forward(random.randint(1,5))
        t2.forward(random.randint(1,5))

        if t1.xcor() > 280:
            pen.write("RED TURTLE WINS!", align="center", font=("Arial", 18, "bold"))
            break
        if t2.xcor() > 280:
            pen.write("BLUE TURTLE WINS!", align="center", font=("Arial", 18, "bold"))
            break

    screen.mainloop()

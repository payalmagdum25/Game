import turtle
import random

def start_game():
    screen = turtle.Screen()
    screen.title("Catch The Turtle")
    screen.bgcolor("white")

    score = 0

    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.speed(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 260)

    def update_score():
        pen.clear()
        pen.write(f"Score : {score}", align="center", font=("Arial", 18, "bold"))

    def move():
        t.goto(random.randint(-250,250), random.randint(-250,250))
        screen.ontimer(move, 1000)

    def catch(x, y):
        nonlocal score
        score += 1
        update_score()
        move()

    def exit_game():
        screen.bye()

    t.onclick(catch)
    screen.onkey(exit_game, "q")
    screen.listen()

    update_score()
    move()
    screen.mainloop()

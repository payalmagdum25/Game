import turtle

def start_game():
    screen = turtle.Screen()
    screen.title("Moving Square Game")
    screen.bgcolor("lightblue")

    player = turtle.Turtle()
    player.shape("square")
    player.penup()
    player.speed(0)

    def up(): player.sety(player.ycor() + 20)
    def down(): player.sety(player.ycor() - 20)
    def left(): player.setx(player.xcor() - 20)
    def right(): player.setx(player.xcor() + 20)
    def exit_game(): screen.bye()

    screen.listen()
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    screen.onkey(exit_game, "q")

    screen.mainloop()

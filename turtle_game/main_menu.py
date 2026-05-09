print("🐢 TURTLE MINI GAME PROJECT 🐢")
print("1. Moving Square")
print("2. Catch The Turtle")
print("3. Turtle Race")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    import game1_moving_square
    game1_moving_square.start_game()

elif choice == "2":
    import game2_catch_turtle
    game2_catch_turtle.start_game()

elif choice == "3":
    import game3_turtle_race
    game3_turtle_race.start_game()

else:
    print("Invalid choice")

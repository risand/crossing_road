from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.level_number = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level_number}", font=FONT)

    def game_over(self):
        self.goto(-90, 0)
        self.write("GAME OVER", font=FONT)

    def increase_level(self):
        self.level_number += 1
        self.update_scoreboard()


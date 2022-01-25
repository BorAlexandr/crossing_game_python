from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-260, 260)
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.increment_level()

    def increment_level(self):
        self.clear()
        self.write(f"Level {self.level}", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard:
    def __init__(self):
        self.text = Turtle()
        self.level = 1
        self.show_level()

    def show_level(self):
        self.text.hideturtle()
        self.text.penup()
        self.text.pencolor("#00FFFF")
        self.text.goto(-280, 230)
        self.text.write(f"Level: {self.level}", font=FONT)

    def clear(self):
        self.text.clear()

    def game_over(self):
        self.text.hideturtle()
        self.text.penup()
        self.text.pencolor("black")
        self.text.goto(-280, 0)
        self.text.write("GAME OVER\nPress Intro to reset\nEsc to Exit", font=FONT)

    def restart(self):
        self.clear()
        self.level = 1
        self.show_level()

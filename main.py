import time
import turtle
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle.register_shape("road.gif")
bg = Turtle()
bg.shape("road.gif")

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('skyblue')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()


def restart():
    global paused
    paused = False
    car.restart()
    player.set_turtle()
    scoreboard.restart()


def turn_off():
    global game_is_on
    game_is_on = not game_is_on


screen.onkey(turn_off, "Escape")
screen.onkey(None, "Return")

car = CarManager()
screen.listen()
car.generate_cars()
paused = False
game_is_on = True
while game_is_on:
    if not paused:
        screen.onkeypress(player.move, "space")
        car.generate_cars()
        level = scoreboard.level
        car.move_cars(level)
        if player.on_finish_line():
            player.set_turtle()
            scoreboard.level += 1
            scoreboard.clear()
            scoreboard.show_level()
        if car.car_crashed(player):
            paused = True
            screen.onkeypress(None, "space")
            scoreboard.game_over()
            screen.onkey(restart, "Return")
        time.sleep(0.1)
        screen.update()
    screen.update()
    screen.delay(100)
screen.bye()

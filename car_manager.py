import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_cars(self):
        dice = random.randint(1, 6)
        if dice == 1:
            car = Turtle()
            car.shape("square")
            car.setheading(180)
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.goto(340, random.randint(-250, 290))
            self.cars.append(car)

    def move_cars(self, level):
        increment = (level - 1) * MOVE_INCREMENT
        for i in self.cars:
            if level == 1:
                i.fd(STARTING_MOVE_DISTANCE)
            else:
                i.fd(STARTING_MOVE_DISTANCE + increment)

    def car_crashed(self, player):
        for i in self.cars:
            if i.distance(player) < 20:
                return True

    def restart(self):
        for i in self.cars:
            i.goto(1000,1000)
        self.cars = []

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT


    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2)
            car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            car.goto(300, new_y)
            self.all_cars.append(car)

    def car_move(self):
        for car in self.all_cars:
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())

    def increment_speed(self):
        self.starting_move_distance += self.move_increment




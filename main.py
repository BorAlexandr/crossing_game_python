import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()
car_manager = CarManager()



turtle.listen()
turtle.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    if player.ycor() == 280:
        player.next_level()
        score_board.increment_level()
        car_manager.increment_speed()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_is_on = False

turtle.exitonclick()


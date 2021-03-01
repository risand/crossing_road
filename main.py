import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.moving()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
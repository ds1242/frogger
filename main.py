import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Frogger')

game_is_on = True

frogger = Player()

screen.listen()
screen.onkey(frogger.move, 'Up')


while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()

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
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(frogger.move, 'Up')


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # collision with car
    for car in car_manager.all_cars:
        if car.distance(frogger) < 20:
            scoreboard.game_over()
            game_is_on = False

    # successful crossing
    if frogger.is_at_finish():
        frogger.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()

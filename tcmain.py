import sys
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
from display import Display

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#2F2F2F")
screen.title("Turtle Crossing Game")
screen.tracer(0)

game_is_on = False

def play_game():
    screen.clear()
    screen.bgcolor("#2F2F2F")
    screen.tracer(0)
    screen.listen()

    display = Display()
    display.road()

    player = Player()
    car = CarManager()
    score = Scoreboard()

    screen.onkey(player.move_forward, "Up")
    screen.onkey(player.move_backward, "Down")
    screen.onkey(start, "Escape")

    global game_is_on
    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car.create_cars()
        car.move_cars()

        for cars in car.all_cars:
            if cars.distance(player) < 30:
                game_is_on = False
                score.game_over()
                start()

        if player.ycor() == FINISH_LINE_Y:
            score.increase_level()
            player.goto(STARTING_POSITION)
            car.increase_speed()

def start():
    global game_is_on
    game_is_on = False
    inp = screen.numinput("New Game", "\n1.Play New Game\n2.Exit\nEnter Your Choice", minval=1, maxval=2)
    if inp == 1:
        play_game()
    elif inp == 2:
        sys.exit()
start()

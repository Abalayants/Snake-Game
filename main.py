from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

"""Creating the GUI for the game and the snake/food/scoreboard instance"""
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Segments")
snake = Snake()
food = Food()
keep_score = Scoreboard()

screen.listen()
"""
Creating the 4 direction by binding the keys with defined functions from the Snake class (See snake.py)
"""
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    """
    Update screen when turtle moves
    Time between refreshes is set really short so that there isn't any glitching
    Move snake
    """
    screen.update()
    time.sleep(0.1)
    snake.move()
    """Detect collision with food"""
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        keep_score.increase_score()
    """Detect wall collision by checking proximity to wall coordinates"""
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        keep_score.reset()
        snake.reset()

    """Detect collision with tail"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            keep_score.game_over()
            keep_score.reset()
            snake.reset()


screen.exitonclick()

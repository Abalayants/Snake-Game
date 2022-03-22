from turtle import Turtle
import time

"""Create constants for ease of manipulation"""
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        """Setting up the scoreboard parameters and placement"""
        self.score = 0
        with open("high score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.speed("fastest")
        self.update_scoreboard()  # Shows updated scoreboard

    def reset(self):
        """Reset scoreboard and write to high score file if new score > current high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear scoreboard and make sure the high score from the file is current"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Needs to show GAME OVER and then move the scoreboard back to original position"""
        self.goto(0, 0)
        self.write(f"GAME OVER! FINAL SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.goto(0, 280)

    def increase_score(self):
        self.score += 1
        # Clear each time so that the score is overwritten and not written on top of old one
        self.clear()
        self.update_scoreboard()

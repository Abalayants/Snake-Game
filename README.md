<h1>About the Project</h1>

A full snake game using Turtle library to create all the elements of the game including the GUI, snake, scoreboard, and "food."

<h2>Process</h2>

Snake Class (Turtle):
1. Has static starting position, directions, and move distance.
2. Creates a starting snake containing three segments and a leader "head."
3. Object able to reset itself, create a new snake every time there is a new game.
4. Segments must all follow each other and be able to move UP, DOWN, LEFT, and RIGHT only.

Scoreboard Class (Turtle):
1. Uses Turtle class to display score at top of screen.
2. Resets scoreboard every time a new game is started, and maintains/updates player score as snake captures more food.
3. Maintains a high score in a file which is recalled everytime a new game starts. Updates the high score if player score > current high score.

Food Class (Turtle):
1. Creates a food object that is placed on screen in random positions, and moves it once snake has made contact with food object.

<h2>Libraries</h2>

<b>Time</b>: Necessary for pause after collision, and also to quickly refresh screen to simulate clean snake movement.

<b>Turtle</b>: Screen, snake segements, food, and scoreboard are all created using Turtle class. 

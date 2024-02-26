from tkinter import *
import random
from Snake import Snake
from Food import Food
from Controller import Controller

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
UNITS_SIZE = 50
CANVAS_BG = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
SNAKE_SPEED = 500  # in miliseconds
score = 0
game_over = False


def gameLoop():
    global score, game_over, snake, food
    if game_over:
        return
    snake.move(controller.new_direction, food.getCoordinates())
    if snake.checkCollision():
        game_over = True
        score_label.config(text="Score: " + str(score) + "  Game over!")
        play_again.pack()
    else:
        snake.updateDrawing(food_coordinates=food.getCoordinates())
        if snake.checkIfSnakeEats(food.getCoordinates()):
            snake.beginning = False
            food.setNewCoordinates()
            score += 1
            score_label.config(text="Score: " + str(score))
    window.after(SNAKE_SPEED, gameLoop)


window = Tk()
window.title("Snake game")
window.state("zoomed")

# create the score label
score_label = Label(
    master=window,
    text="Score: " + str(score),
    font=("Sans Serif", 50),
    bg="lightblue",
)
score_label.pack(fill="x")

# create the canvas
canvas = Canvas(
    master=window,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    bg=CANVAS_BG,
)
canvas.pack()

# create the controller
controller = Controller(window, "right")


# create the snake
def createSnake():
    global CANVAS_WIDTH, CANVAS_HEIGHT, UNITS_SIZE
    initial_head_x_coord = CANVAS_WIDTH / 2
    initial_head_y_coord = CANVAS_HEIGHT / 2
    snake = Snake(
        canvas=canvas,
        canvas_width=CANVAS_WIDTH,
        canvas_height=CANVAS_HEIGHT,
        units_size=UNITS_SIZE,
        color=SNAKE_COLOR,
        initial_head_x_coord=initial_head_x_coord,
        initial_head_y_coord=initial_head_y_coord,
    )
    snake.direction = controller.new_direction  # initial direction
    return snake


snake = createSnake()


# create the food
def createFood():
    global CANVAS_WIDTH, CANVAS_HEIGHT, UNITS_SIZE
    initial_x_coord = random.randint(0, CANVAS_WIDTH / UNITS_SIZE - 1) * UNITS_SIZE
    initial_y_coord = random.randint(0, CANVAS_HEIGHT / UNITS_SIZE - 1) * UNITS_SIZE
    food = Food(
        canvas=canvas,
        canvas_width=CANVAS_HEIGHT,
        canvas_height=CANVAS_HEIGHT,
        units_size=UNITS_SIZE,
        color=FOOD_COLOR,
        initial_x_coord=initial_x_coord,
        initial_y_coord=initial_y_coord,
    )
    return food


food = createFood()

# start the game
gameLoop()


def playAgain():
    global game_over, score, snake, food, canvas
    canvas.destroy()
    canvas = Canvas(
        master=window,
        width=CANVAS_WIDTH,
        height=CANVAS_HEIGHT,
        bg=CANVAS_BG,
    )
    canvas.pack()
    game_over = False
    score = 0
    score_label.config(text="Score: " + str(score))
    snake = createSnake()
    food = createFood()
    play_again.pack_forget()
    gameLoop()
    window.update()


play_again = Button(
    master=window,
    text="Play again?",
    font=("Sans Serif", 40),
    command=playAgain,
)

window.mainloop()

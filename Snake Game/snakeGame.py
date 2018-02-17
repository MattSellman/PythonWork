from turtle import Turtle, Screen
import random

# size of snake cubes
Size = 20


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawSelf(self, turtle):
        screen.screensize(300, 300)
        # draw a black box, leaving gaps between cubes
        turtle.goto(self.x - Size // 2 - 1, self.y - Size // 2 - 1)

        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(Size - Size // 10)
            turtle.left(90)
        turtle.end_fill()


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def changeLocation(self):
        # program to spawn outside snakes body
        self.x = random.randint(0, Size) * Size - 200
        self.y = random.randint(0, Size) * Size - 200

    def drawSelf(self, turtle):
        # similar to the sqr but different purposes
            turtle.goto(self.x - Size // 2 - 1, self.y - Size // 2 - 1)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(Size - Size // 10)
                turtle.left(90)
            turtle.end_fill()


class Snake:
    body = None                # x,y coordinates for snake
    headPosition = None

    def __init__(self):
        self.headPosition = [Size, 0]  # keep track of where we go next
        self.body = [Square(-Size, 0), Square(0, 0), Square(Size, 0)]
        self.nextX = 1  # which way snake goes next
        self.nextY = 0
        self.crashed = False  # for collisions
        self.nextPosition = [self.headPosition[0] + Size * self.nextX, self.headPosition[1] + Size * self.nextY]
        # prepare next location for adding snake

    # movement here
    def moveUp(self):
        self.nextX, self.nextY = 0, 1

    def moveLeft(self):
        self.nextX, self.nextY = -1, 0

    def moveRight(self):
        self.nextX, self.nextY = 1, 0

    def moveDown(self):
        self.nextX, self.nextY = 0, -1

    def eatFood(self):
        # extends the snake by 1 each time good is eaten
        self.body.append(Square(self.nextPosition[0], self.nextPosition[1]))
        self.headPosition[0], self.headPosition[1] = self.body[-1].x, self.body[-1].y
        self.nextPosition = [self.headPosition[0] + Size * self.nextX, self.headPosition[1] + Size * self.nextY]

    def drawSelf(self, turtle):  # draw snake when called
        for segment in self.body:
            segment.drawSelf(turtle)

    def moveOneStep(self):
        if Square(self.nextPosition[0], self.nextPosition[1]) not in self.body:
            # attempt (unsuccessful) at collision detection
            self.body.append(Square(self.nextPosition[0], self.nextPosition[1]))
            # moves the snake head to the next spot, deleting the tail
            del self.body[0]
            self.headPosition[0], self.headPosition[1] = self.body[-1].x, self.body[-1].y
            # resets the head and nextposition
            self.nextPosition = [self.headPosition[0] + Size * self.nextX, self.headPosition[1] + Size * self.nextY]
        else:
            self.crashed = True  # more unsuccessful collision detection


class Game:
    def __init__(self):
        # game objects: screen, turtle, snake, food
        self.screen = Screen()
        self.artist = Turtle(visible=False)
        self.artist.up()
        self.artist.speed("slowest")

        self.snake = Snake()
        self.food = Food(100, 0)

        # used for later (see where)
        self.counter = 0
        self.commandPending = False
        self.screen.tracer(0)  # follow the snake

        self.screen.listen()
        self.screen.onkey(self.snakeDown, "Down")
        self.screen.onkey(self.snakeUp, "Up")
        self.screen.onkey(self.snakeLeft, "Left")
        self.screen.onkey(self.snakeRight, "Right")



    def nextFrame(self):
        self.artist.clear()

        if (self.snake.nextPosition[0], self.snake.nextPosition[1]) == (self.food.x, self.food.y):
            self.snake.eatFood()
            self.food.changeLocation()
        else:
            self.snake.moveOneStep()

        if self.counter == 10:
            self.counter = 0
        else:
            self.counter += 1

        self.food.drawSelf(self.artist)  # show food and snake
        self.snake.drawSelf(self.artist)
        self.screen.update()
        self.screen.ontimer(lambda: self.nextFrame(), 100)

    def snakeUp(self):
        if not self.commandPending:
            self.commandPending = True
            self.snake.moveUp()
            self.commandPending = False

    def snakeDown(self):
        if not self.commandPending:
            self.commandPending = True
            self.snake.moveDown()
            self.commandPending = False

    def snakeLeft(self):
        if not self.commandPending:
            self.commandPending = True
            self.snake.moveLeft()
            self.commandPending = False

    def snakeRight(self):
        if not self.commandPending:
            self.commandPending = True
            self.snake.moveRight()
            self.commandPending = False


game = Game()
screen = Screen()
screen.ontimer(lambda: game.nextFrame(), 100)
screen.mainloop()
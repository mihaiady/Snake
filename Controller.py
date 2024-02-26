class Controller:
    def __init__(self, window, initial_direction):
        window.bind("<Up>", self.moveUp)
        window.bind("<Down>", self.moveDown)
        window.bind("<Left>", self.moveLeft)
        window.bind("<Right>", self.moveRight)
        self.new_direction = initial_direction

    def moveUp(self, event):
        self.new_direction = "up"

    def moveDown(self, event):
        self.new_direction = "down"

    def moveLeft(self, event):
        self.new_direction = "left"

    def moveRight(self, event):
        self.new_direction = "right"

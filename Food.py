import random


class Food:
    def __init__(
        self,
        canvas,
        canvas_width,
        canvas_height,
        units_size,
        color,
        initial_x_coord,
        initial_y_coord,
    ):
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        canvas_height,
        self.units_size = units_size
        self.color = color
        self.coordinates = [initial_x_coord, initial_y_coord]
        self.body = canvas.create_oval(
            initial_x_coord,
            initial_y_coord,
            initial_x_coord + self.units_size,
            initial_y_coord + self.units_size,
            fill=self.color,
            tag="food",
        )

    def getCoordinates(self):
        return self.coordinates

    def setNewCoordinates(self):
        x = random.randint(0, self.canvas_width / self.units_size - 1) * self.units_size
        y = (
            random.randint(0, self.canvas_height / self.units_size - 1)
            * self.units_size
        )
        self.coordinates = [x, y]
        self.canvas.delete(self.canvas.find_withtag("food")[0])
        self.canvas.create_oval(
            self.coordinates[0],
            self.coordinates[1],
            self.coordinates[0] + self.units_size,
            self.coordinates[1] + self.units_size,
            fill=self.color,
            tag="food",
        )

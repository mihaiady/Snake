class Snake:
    def __init__(
        self,
        canvas,
        canvas_width,
        canvas_height,
        units_size,
        color,
        initial_head_x_coord,
        initial_head_y_coord,
    ):
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.units_size = units_size
        self.color = color
        # index 0 represents the head
        self.snake_coordinates = [[initial_head_x_coord, initial_head_y_coord]]
        canvas.create_rectangle(
            initial_head_x_coord,
            initial_head_y_coord,
            initial_head_x_coord + units_size,
            initial_head_y_coord + units_size,
            fill=color,
            tag="snake",
        )
        self.current_direction = None
        self.directions = {
            "up": [0, -1],
            "down": [0, 1],
            "left": [-1, 0],
            "right": [1, 0],
        }
        # will tell if there is only one element in the snake's body
        self.beginning = True

    def move(self, new_direction, food_coordinates):
        if (
            (new_direction == "up" and self.current_direction == "down")
            or (new_direction == "down" and self.current_direction == "up")
            or (new_direction == "left" and self.current_direction == "right")
            or (new_direction == "right" and self.current_direction == "left")
        ) and self.beginning == False:
            new_direction = self.current_direction
        new_head_x_coord = (
            self.snake_coordinates[0][0]
            + self.directions[new_direction][0] * self.units_size
        )
        new_head_y_coord = (
            self.snake_coordinates[0][1]
            + self.directions[new_direction][1] * self.units_size
        )
        self.snake_coordinates.insert(0, [new_head_x_coord, new_head_y_coord])
        if self.snake_coordinates[0] != food_coordinates:
            self.snake_coordinates.pop()
        self.current_direction = new_direction

    def updateDrawing(self, food_coordinates):
        self.canvas.create_rectangle(
            self.snake_coordinates[0][0],
            self.snake_coordinates[0][1],
            self.snake_coordinates[0][0] + self.units_size,
            self.snake_coordinates[0][1] + self.units_size,
            fill=self.color,
            tag="snake",
        )
        if self.snake_coordinates[0] != food_coordinates:
            self.canvas.delete(self.canvas.find_withtag("snake")[0])

    def checkIfSnakeEats(self, food_coordinates):
        return True if self.snake_coordinates[0] == food_coordinates else False

    def checkCollision(self):
        head_x_coord = self.snake_coordinates[0][0]
        head_y_coord = self.snake_coordinates[0][1]
        if (
            head_x_coord < 0
            or head_x_coord >= self.canvas_width
            or head_y_coord < 0
            or head_y_coord >= self.canvas_height
        ):
            return True
        snake_length = len(self.snake_coordinates)
        if snake_length > 1:
            for index in range(1, snake_length):
                if (
                    self.snake_coordinates[index][0] == head_x_coord
                    and self.snake_coordinates[index][1] == head_y_coord
                ):
                    return True
        return False

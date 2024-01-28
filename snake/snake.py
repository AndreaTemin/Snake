import random
from utils import GAME_CONFIG, DIRECTIONS, fit_the_box

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Snake:
    def __init__(self):
        self.length = 1
        center = (GAME_CONFIG['WIDTH']//2), (GAME_CONFIG["HEIGHT"] // 2)
        self.positions = [fit_the_box(*center)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # 0: up, 1:down, 2:left, 3:right

    def get_head_position(self):
        return self.positions[0]
    
    def get_tail_positions(self):
        return self.positions[1:]
    
    def move(self):
        current = self.get_head_position()
        x, y = current

        grid_size = GAME_CONFIG["GRID_SIZE"]

        if self.direction == DIRECTIONS["UP"]:
            y -= grid_size
        elif self.direction == DIRECTIONS["DOWN"]:
            y += grid_size
        elif self.direction == DIRECTIONS["LEFT"]:
            x -= grid_size
        elif self.direction == DIRECTIONS["RIGHT"]:
            x += grid_size

        self.positions = [(x,y)] + self.positions[:-1]

    def reset(self):
        self.__init__()


if __name__ == "__main__":
    pass





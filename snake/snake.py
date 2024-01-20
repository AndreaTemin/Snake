import random
from utils import GAME_CONFIG, DIRECTIONS

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((GAME_CONFIG['WIDTH']//2), (GAME_CONFIG["HEIGHT"] // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # 0: up, 1:down, 2:left, 3:right

    def get_head_position(self):
        return self.positions[0]
    
    def move(self):
        current = self.get_head_position()
        x, y = current

        if self.direction == DIRECTIONS["UP"]:
            y -= GAME_CONFIG["GRID_SIZE"]
        elif self.direction == DIRECTIONS["DOWN"]:
            y += GAME_CONFIG["GRID_SIZE"]
        elif self.direction == DIRECTIONS["LEFT"]:
            x -= GAME_CONFIG["GRID_SIZE"]
        elif self.direction == DIRECTIONS["RIGHT"]:
            x += GAME_CONFIG["GRID_SIZE"]

        self.positions = [(x,y)] + self.positions[:-1]

    def reset(self):
        self.__init__()


if __name__ == "__main__":
    s = Snake()
    print(s.get_head_position())
    s.direction = UP
    s.move()
    print(s.get_head_position())





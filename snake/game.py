
import pygame
import sys 
import random
from snake import Snake
from utils import GAME_CONFIG as config, DIRECTIONS as dir, fit_the_box

GAME_CONFIG = config
DIRECTIONS = dir

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = self.place_food()
       
    def place_food(self):
        width = GAME_CONFIG["WIDTH"]
        height = GAME_CONFIG["HEIGHT"]
        # can do better by chosing between all the 
        
        # the -1 allows the food not to spown outside of the screen
        x,y = random.randint(0,width-1), random.randint(0,height)
        while fit_the_box(x,y) in self.snake.get_tail_positions() :   
            x,y = random.randint(0,width-1), random.randint(0,height)
        
        return fit_the_box(x,y)
    
    def render(self, surface):
        # Draw Snake head
        pygame.draw.rect(surface, GAME_CONFIG["HEAD_COLOR"],
                             (*self.snake.get_head_position(), GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))
        # Draw rest of Snake
        for i, pos in enumerate(self.snake.positions[1:]):
            # this will gradually change the color of the snake
            color = (5+i, GAME_CONFIG["SNAKE_COLOR"][1]-i*2, 5+i)
            pygame.draw.rect(surface, color, # this will change the color of the snake gradually 
                             (*pos, GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))

        # Draw food
        pygame.draw.rect(surface, GAME_CONFIG["RED"],
                          (*self.food,GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))

    def game_over(self):
        self.__init__()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                d = self.snake.direction
                next_direction = {
                    pygame.K_DOWN: DIRECTIONS["DOWN"] if d not in {DIRECTIONS["UP"],DIRECTIONS["DOWN"]} else d,
                    pygame.K_UP: DIRECTIONS["UP"] if d not in {DIRECTIONS["UP"],DIRECTIONS["DOWN"]} else d,
                    pygame.K_LEFT: DIRECTIONS["LEFT"] if d not in {DIRECTIONS["LEFT"],DIRECTIONS["RIGHT"]} else d,
                    pygame.K_RIGHT: DIRECTIONS["RIGHT"] if d not in {DIRECTIONS["LEFT"],DIRECTIONS["RIGHT"]} else d
                }
                direction = next_direction.get(event.key)
                self.snake.direction = direction if direction is not None else self.snake.direction
                pygame.time.delay(1)    
    
    
    def update(self):
        self.snake.move()
        head = self.snake.get_head_position()
 
        # hitting the border
        if not (GAME_CONFIG['WIDTH'] > head[0] >= 0 and GAME_CONFIG['HEIGHT'] > head[1] >= 0):
            self.game_over()

        # eating tail
        if head in self.snake.get_tail_positions():
            self.game_over()
          
        # event eating food
        if head == self.food:
            self.snake.length += 1
            self.snake.positions.append(self.food)
            self.food = self.place_food()
        
        
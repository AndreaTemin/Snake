
import pygame
import sys 
import random
from snake import Snake
from utils import GAME_CONFIG, DIRECTIONS, fit_the_box

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = self.place_food()

    def place_food(self):
        x,y = random.randint(0,GAME_CONFIG["WIDTH"]), random.randint(0,GAME_CONFIG["HEIGHT"])
        return fit_the_box(x,y)
    
    def render(self, surface):
        # Draw Snake head
        pygame.draw.rect(surface, GAME_CONFIG["HEAD_COLOR"],
                             (*self.snake.get_head_position(), GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))
        # Draw rest of Snake
        for i, pos in enumerate(self.snake.positions[1:]):
            # this will change the color of the snake gradually
            color = (5, GAME_CONFIG["SNAKE_COLOR"][1]-i*1, 5)
            pygame.draw.rect(surface, color, # this will change the color of the snake gradually 
                             (*pos, GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))

        # Draw food
        pygame.draw.rect(surface, GAME_CONFIG["RED"],
                          (*self.food,GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))

    def game_over(self):
        self.__init__()

    def handle_evets(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP and
                   (self.snake.direction != DIRECTIONS["UP"] and self.snake.direction != DIRECTIONS["DOWN"])):
                    self.snake.direction = DIRECTIONS["UP"]
                    return
                elif (event.key == pygame.K_DOWN and
                     (self.snake.direction != DIRECTIONS["DOWN"] and self.snake.direction != DIRECTIONS["UP"])):
                    self.snake.direction = DIRECTIONS["DOWN"]
                    return
                elif (event.key == pygame.K_LEFT and
                     (self.snake.direction != DIRECTIONS["RIGHT"] and self.snake.direction != DIRECTIONS["LEFT"])):
                    self.snake.direction = DIRECTIONS["LEFT"]
                    return
                elif (event.key == pygame.K_RIGHT and
                     (self.snake.direction != DIRECTIONS["LEFT"] and self.snake.direction != DIRECTIONS["RIGHT"])):
                    self.snake.direction = DIRECTIONS["RIGHT"]
                    return

                elif (event.key == pygame.K_DELETE):
                    self.snake.reset()
                    self.food = self.place_food()

    def update(self):
        self.snake.move()
        head = self.snake.get_head_position()

            
        # hitting the border
        if not (GAME_CONFIG['WIDTH'] >= head[0] >= 0 and GAME_CONFIG['HEIGHT'] >= head[1] >= 0):
            self.game_over()

        if head in self.snake.positions[2:]:
            self.game_over()
        
            
        # event eating food
        if head == self.food:
            self.snake.length += 1
            self.snake.positions.append(self.food)
            self.food = self.place_food()
        
        
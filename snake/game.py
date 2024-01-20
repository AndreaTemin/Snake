
import pygame
import sys 
import random
from snake import Snake
from utils import GAME_CONFIG, DIRECTIONS

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = self.place_food()

    def place_food(self):
        x,y = random.randint(0,GAME_CONFIG["WIDTH"]), random.randint(0,GAME_CONFIG["HEIGHT"])
        return (x,y)
    
    def render(self, surface):
        # Draw Snake
        for pos in self.snake.positions:
            pygame.draw.rect(surface, GAME_CONFIG["GREEN"],
                             (*pos, GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))

        # Draw food
        pygame.draw.rect(surface, GAME_CONFIG["RED"],
                          (*self.food,GAME_CONFIG["SNAKE_SIZE"], GAME_CONFIG["SNAKE_SIZE"]))

    def handle_evets(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP and self.snake.direction != DIRECTIONS["DOWN"]):
                    self.snake.direction = DIRECTIONS["UP"]
                elif (event.key == pygame.K_DOWN and self.snake.direction != DIRECTIONS["UP"]):
                    self.snake.direction = DIRECTIONS["DOWN"]
                elif (event.key == pygame.K_LEFT and self.snake.direction != DIRECTIONS["RIGHT"]):
                    self.snake.direction = DIRECTIONS["LEFT"]
                elif (event.key == pygame.K_RIGHT and self.snake.direction != DIRECTIONS["LEFT"]):
                    self.snake.direction = DIRECTIONS["RIGHT"]

                elif (event.key == pygame.K_DELETE):
                    self.snake.reset()
                    self.food = self.place_food()
        pass

    def update(self):
        self.snake.move()

        
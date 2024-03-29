from time import sleep
import pygame
from game import Game
from utils import GAME_CONFIG

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((GAME_CONFIG['WIDTH'], GAME_CONFIG['HEIGHT']), 0, 32)
    pygame.display.set_caption("Snake Game")

    game = Game()

    while True:
        game.handle_events()
        game.update()

        screen.fill(GAME_CONFIG["DARK_GRAY"])
        game.render(screen)
        
        pygame.display.update()

        clock.tick(10)
        


if __name__ == "__main__":
    main()
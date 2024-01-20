# utils.py
# instead of dictinary we could make a pyi file with all the constants
GAME_CONFIG = {
    'WIDTH': 600,
    'HEIGHT': 400,
    'GRID_SIZE': 20,
    'SNAKE_SIZE': 20,
    'DARK_GRAY': (10, 30, 30),
    'WHITE': (255, 255, 255),
    'GREEN' : (5, 240, 5),
    'RED' : (240, 5, 5)
}

DIRECTIONS = {
    "UP" : 0,
    "DOWN" : 1,
    "LEFT" : 2,
    "RIGHT" : 3
}

# given a position (x,y) will give the center of the relative box
def fit_the_box(*position:(int,int)):
    box = GAME_CONFIG["GRID_SIZE"]
    
    x = position[0]//box*box + box//2
    y = position[1]//box*box + box//2

    return x, y

    

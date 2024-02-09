import pygame
import math
import time  # Import time module for delays

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
hud_height = 50  # Height for the HUD at the top of the screen
game_screen_height = screen_height - hud_height  # Adjusted game screen height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Pac-Man')

# Colors
wall_color = (0, 0, 255)  # Blue walls
dot_color = (255, 255, 255)  # White dots
text_color = (255, 255, 255)  # White text

# Maze setup
# Adjusted for HUD space
maze_layout = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W.d............WW.dW",
    "W.WWWW.WWWWW.WW.WWWW",
    "WPWWWW.WWWWW.WW.WWWW",
    "Wd....WW...WW.....dW",
    "W.WWWWWWWWWWWW.WWWW",
    "W...............WdW",
    "WWWWWWWWWWWWWWWWWWWW"
]
maze_row_height = game_screen_height // len(maze_layout)
maze_column_width = screen_width // len(maze_layout[0])

# Pac-Man setup
pacman_color = (255, 255, 0)  # Classic yellow
# Adjust starting position for HUD
pacman_x = 0
pacman_y = hud_height
pacman_direction = 'right'
pacman_speed = maze_column_width // 10
pacman_radius = min(maze_row_height, maze_column_width) // 4
pacman_open_angle = 45

# Font setup for text display
font = pygame.font.Font(None, 36)

# Function to display text
def display_text(message, position, duration=0):
    text = font.render(message, True, text_color)
    screen.blit(text, position)
    if duration > 0:
        pygame.display.update()
        time.sleep(duration)  # Pause for the duration

# Game loop setup
running = True
clock = pygame.time.Clock()

# Display "READY! GO!" sequence at the start
screen.fill((0, 0, 0))  # Clear screen
display_text("READY!", (screen_width // 2 - 50, screen_height // 2 - 10), 1.5)
screen.fill((0, 0, 0))  # Clear screen again for "GO!"
display_text("GO!", (screen_width // 2 - 30, screen_height // 2 - 10), 1.5)

# Rest of the game loop...

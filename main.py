import pygame
import sys
import random
from bird import Bird
from pipe import Pipe
from scoreboard import Scorecard

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
FPS: int = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Variables
paused = False
gameover = False
lst = [
    -130,
    -120,
    -110,
    -100,
    -90,
    -80,
    -70,
    -60,
    -50,
    -40,
    -30,
    -20,
    -10,
    0,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
]
pipes = []
deviation = random.choice(lst)
# deviation = -130
distance_per_frame = 0
distance = 0


# Colors

# Instances
bird = Bird(100, 100, 30, 30)
pipe_1 = Pipe(800, -150 + deviation, 350, 50)
pipe_2 = Pipe(800, 350 + deviation, 350, 50)


# Functions
def check_game_over(player):
    global gameover
    if (player.y + player.height) > HEIGHT:
        gameover = True
        player.velocity = 0
        player.gravity = 0
        player.jump_strength = 0
    elif player.y < 0:
        gameover = True
        player.velocity = 0
        player.jump_strength = 0


# def obstacles():
#     if distance_per_frame / 60 == 0:
#         lenght = len(pipes)
#         pipe_


# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.time.delay(500)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Draw
    screen.fill("skyblue")

    # Update
    bird.s_update(screen)
    pipe_1.s_update(screen)
    pipe_2.s_update(screen)

    check_game_over(bird)
    distance_per_frame += 1
    if distance_per_frame == 61:
        distance_per_frame = 0
        distance += 1
    print(distance)

    # Draw your game objects here
    score = Scorecard(100, 100, screen, str(distance))
    score.draw()
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()

import sys
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1200, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch thex Falling Objects!')

clock = pygame.time.Clock()

player_width, player_height = 50,50
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

object_width, object_height = 30, 30
object_speed = 5
objects = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Allow the player to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    for obj in objects:
        obj['y'] += object_speed

        # Check collision with player
        if (
            player_x < obj['x'] < player_x + player_width
            and player_y < obj['y'] < player_y + player_height
        ):
            objects.remove(obj)

    # Remove objects that are off-screen
    objects = [obj for obj in objects if obj['y'] < HEIGHT]

    # Add a new falling object
    if random.randint(1, 100) < 5:
        object_x = random.randint(0, WIDTH - object_width)
        objects.append({'x': object_x, 'y': 0})

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    for obj in objects:
        pygame.draw.rect(screen, RED, (obj['x'], obj['y'], object_width, object_height))

    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

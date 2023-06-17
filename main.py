import pygame
from fighter import Fighter

pygame.init()

# game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# Define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# load background image
bg_image = pygame.image.load("assets/images/background/vancouver.jpg").convert_alpha()

# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# function for drawing fighters' health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))


# create two instances of fighters
fighter_1 = Fighter(200, 370)
fighter_2 = Fighter(700, 370)

# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    # Show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    # move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # update display
    pygame.display.update()

# exit pygame
pygame.quit()
import pygame
import sys
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
score = 0

pygame.init()  # Start pygame modules

score_font = pygame.font.Font(None, 36)

def choose_random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def choose_random_pos(radius):
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    return (x, y)

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Click The Circle")

clock = pygame.time.Clock()

# Circle settings
circle_x = SCREEN_WIDTH / 2
circle_y = SCREEN_HEIGHT / 2
radius = 40

circle_color = choose_random_colour()

circle_rect = pygame.Rect(circle_x - radius, circle_y - radius, radius * 2, radius * 2)
score_color = (255, 255, 255)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            if circle_rect.collidepoint(event.pos):
                circle_color = choose_random_colour()
                circle_x, circle_y = choose_random_pos(radius)
                score += 1  #updates score here
                score_color = choose_random_colour()
            else:
                score = 0

    # Update hitbox
    circle_rect.center = (circle_x, circle_y)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw circle
    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), radius)

    #draws score every frame
    score_text = score_font.render(f"Score: {score}", True, score_color)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
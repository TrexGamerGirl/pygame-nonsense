import pygame
import sys

pygame.init()  # Start pygame

screen = pygame.display.set_mode((800, 600))  # Create window
pygame.display.set_caption("My First Game")   # Window title

circle_x = 400   # Starting X position
circle_y = 300   # Starting Y position
speed = 5        # How fast it moves

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Get all pressed keys

    if keys[pygame.K_LEFT]:
        circle_x -= speed
    if keys[pygame.K_RIGHT]:
        circle_x += speed
    if keys[pygame.K_UP]:
        circle_y -= speed
    if keys[pygame.K_DOWN]:
        circle_y += speed

    screen.fill((0, 0, 0))  # Fill screen black
    pygame.draw.rect(screen, (132, 3, 252), (100, 100, 200, 150))
    pygame.draw.circle(screen, (140, 3, 252), (circle_x, circle_y), 50)
    pygame.display.flip()   # Update display
   

pygame.quit()
sys.exit()
import pygame
import sys

pygame.init()  # Start pygame

screen = pygame.display.set_mode((800, 600))  # Create window
pygame.display.set_caption("My First Game")   # Window title

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill screen black
    pygame.draw.rect(screen, (132, 3, 252), (100, 100, 200, 150))
    pygame.draw.circle(screen, (252, 3, 169), (400, 300), 50)
    pygame.display.flip()   # Update display
   

pygame.quit()
sys.exit()
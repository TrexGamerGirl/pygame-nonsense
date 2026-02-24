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
    pygame.display.flip()   # Update display

pygame.quit()
sys.exit()
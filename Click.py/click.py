import pygame
import sys
from random import randint

def choose_random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)  # return a random RGB colour

pygame.init()  # Start pygame modules

# Create window
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Click The Circle")

clock = pygame.time.Clock()  # Controls FPS

# Circle settings
circle_x = 400
circle_y = 300
radius = 40

# These velocities are unused now so the circle stays stationary
velocity_x = 0
velocity_y = 0

circle_color = choose_random_colour()

# Create a rectangular hitbox for the circle so we can detect clicks
circle_rect = pygame.Rect(circle_x - radius, circle_y - radius, radius*2, radius*2)

running = True
while running:
    clock.tick(60)  # Lock to 60 FPS (important for consistent movement)

    for event in pygame.event.get():  # Process all events

        if event.type == pygame.QUIT:
            running = False  # Close the game window

        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            if circle_rect.collidepoint(event.pos):  # Check if click is inside the circle hitbox
                circle_color = choose_random_colour()  # Change the circle colour

    width, height = screen.get_size()  # Get current window size

    # Update hitbox position (keeps it aligned with the circle)
    circle_rect.center = (circle_x, circle_y)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw circle
    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), radius)

    pygame.display.flip()  # Update screen

pygame.quit()
sys.exit()
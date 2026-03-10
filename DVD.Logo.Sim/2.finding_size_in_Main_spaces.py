import pygame
import sys
from random import randint
def choose_random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


pygame.init()  # Start pygame modules

# Create window
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("DVD Logo Simulator")

clock = pygame.time.Clock()  # Controls FPS

# Circle settings
circle_x = 400
circle_y = 300
radius = 40

velocity_x = 5  # Horizontal movement speed
velocity_y = 4  # Vertical movement speed

circle_color = choose_random_colour()

running = True
while running:
    clock.tick(60)  # Lock to 60 FPS (important for consistent movement)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the circle
    circle_x += velocity_x
    circle_y += velocity_y

    width, height = screen.get_size()  # Get current window size

    # Bounce off LEFT or RIGHT walls
    if circle_x - radius <= 0:
        circle_x = radius  # Prevent sticking inside wall
        velocity_x *= -1   # Reverse horizontal direction

        circle_color = choose_random_colour()

    
    if circle_x + radius >= width:
        circle_x = width - radius
        velocity_x *= -1

        circle_color = choose_random_colour()

    # Bounce off TOP or BOTTOM walls
    if circle_y - radius <= 0:
        circle_y = radius
        velocity_y *= -1   # Reverse vertical direction

        circle_color = choose_random_colour()

    if circle_y + radius >= height:
        circle_y = height - radius
        velocity_y *= -1

        circle_color = choose_random_colour()

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw circle
    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), radius)

    pygame.display.flip()  # Update screen

pygame.quit()
sys.exit()
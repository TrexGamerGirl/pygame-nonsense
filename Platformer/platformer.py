import pygame
import sys

# =============================
# INITIAL SETUP
# =============================
pygame.init()  # Start pygame

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")

clock = pygame.time.Clock()
FPS = 60

# =============================
# PLAYER SETTINGS
# =============================
player = pygame.Rect(100, 100, 40, 60)  # x, y, width, height
player_vel_y = 0  # vertical velocity
GRAVITY = 0.5
JUMP_STRENGTH = -10
MOVE_SPEED = 5
on_ground = False

# =============================
# PLATFORM SETUP
# =============================
platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(400, 350, 150, 20),
    pygame.Rect(600, 250, 150, 20)
]

# =============================
# MAIN GAME LOOP
# =============================
running = True
while running:
    clock.tick(FPS)

    # =========================
    # EVENTS (INPUT HANDLING)
    # =========================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Jump when SPACE is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                player_vel_y = JUMP_STRENGTH

    # =========================
    # MOVEMENT INPUT
    # =========================
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= MOVE_SPEED
    if keys[pygame.K_d]:
        player.x += MOVE_SPEED

    # =========================
    # APPLY GRAVITY
    # =========================
    player_vel_y += GRAVITY
    player.y += player_vel_y

    # =========================
    # COLLISION DETECTION
    # =========================
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            # Only land if falling
            if player_vel_y > 0:
                player.bottom = platform.top
                player_vel_y = 0
                on_ground = True

    # =========================
    # SCREEN DRAWING
    # =========================
    screen.fill((30, 30, 30))  # background color

    # Draw player
    pygame.draw.rect(screen, (0, 200, 255), player)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (100, 255, 100), platform)

    pygame.display.flip()  # update screen

# =============================
# CLEAN UP
# =============================
pygame.quit()
sys.exit()

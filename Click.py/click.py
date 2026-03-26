import pygame
import sys
from tkinter import messagebox
from random import randint
from pathlib import Path
import csv


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
score = 0

pygame.init()

score_font = pygame.font.Font(None, 36)

# Get the folder where this script (Click.py) is located
BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "scores.csv"


def choose_random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def choose_random_pos(radius):
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    return (x, y)


# Ensure CSV file exists
def Is_CSV_File():
    if not CSV_FILE.exists():
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Score"])  # header row


# Save score to CSV
def save_score(score):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([score])


# Read scores and return top 10
def get_top_scores():
    scores = []

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header

        for row in reader:
            if row:
                scores.append(int(row[0]))

    scores.sort(reverse=True)
    return scores[:10]


# Make sure file exists before game starts
Is_CSV_File()


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
                score += 1
                score_color = choose_random_colour()
            else:
                # Save score
                save_score(score)

                # Load leaderboard
                top_scores = get_top_scores()

                leaderboard_text = "\n".join(
                    [f"{i+1}. {s}" for i, s in enumerate(top_scores)]
                )

                # Show message with file location included
                messagebox.showinfo(
                    "Game Over",
                    f"You lost!\n\n"
                    f"Your score: {score}\n\n"
                    f"Top 10 Scores:\n{leaderboard_text}\n\n"
                    f"Scores saved to:\n{CSV_FILE}"
                )

                pygame.quit()
                sys.exit()

    circle_rect.center = (circle_x, circle_y)

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), radius)

    score_text = score_font.render(f"Score: {score}", True, score_color)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
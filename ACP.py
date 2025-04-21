import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load background image
background = pygame.image.load("background.png").convert()

# Load and play background music
pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Define enemy class
class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.x = x
        self.y = y
        self.speed = random.randint(2, 5)

    def move(self):
        self.x += self.speed
        if self.x <= 0 or self.x >= WIDTH - 50:  # Bounce back when hitting edges
            self.speed *= -1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Create a list of enemies
enemies = []
for i in range(7):  # Create 7 enemies
    x = random.randint(50, WIDTH - 100)
    y = random.randint(50, 200)
    enemies.append(Enemy(x, y))

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.blit(background, (0, 0))  # Draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw each enemy
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

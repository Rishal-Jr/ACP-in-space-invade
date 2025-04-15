import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)

# Load player sprite
player = pygame.image.load("player.png")
player_rect = player.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))

# Load enemy sprites
enemy_img = pygame.image.load("enemy.png")
enemies = [pygame.Rect(random.randint(0, WIDTH - 50), random.randint(50, HEIGHT - 200), 50, 50) for _ in range(7)]

# Score tracking
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

    # Collision detection
    for enemy_rect in enemies:
        if player_rect.colliderect(enemy_rect):
            score += 1
            enemy_rect.x, enemy_rect.y = random.randint(0, WIDTH - 50), random.randint(50, HEIGHT - 200)  # Reset position

    # Drawing
    screen.blit(player, player_rect)
    for enemy_rect in enemies:
        screen.blit(enemy_img, enemy_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()

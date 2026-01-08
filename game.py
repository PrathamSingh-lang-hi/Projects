import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Bounce")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
YELLOW = (255, 255, 0)

# Paddle
paddle = pygame.Rect(WIDTH//2 - 60, HEIGHT - 30, 120, 15)

# Ball
ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 20, 20)
ball_speed = [4, -4]
base_speed = 4
speed_timer = pygame.time.get_ticks()

# Blocks
block_rows = 5
block_cols = 10
block_width = WIDTH // block_cols
block_height = 30
blocks = [pygame.Rect(col * block_width, row * block_height, block_width - 2, block_height - 2)
          for row in range(block_rows) for col in range(block_cols)]

# Power-ups
powerups = []
POWERUP_TYPES = ['extend', 'slow', 'score']
powerup_size = 20

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(6, 0)

    # Ball movement
    ball.move_ip(ball_speed[0], ball_speed[1])

    # Speed increase over time
    if pygame.time.get_ticks() - speed_timer > 15000:
        base_speed += 1
        ball_speed[0] = base_speed if ball_speed[0] > 0 else -base_speed
        ball_speed[1] = -base_speed
        speed_timer = pygame.time.get_ticks()

    # Bounce off walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1

    # Bounce off paddle
    if ball.colliderect(paddle):
        ball_speed[1] *= -1

    # Bounce off blocks
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        hit_block = blocks.pop(hit_index)
        ball_speed[1] *= -1
        score += 10

        # Random chance to drop powerup
        if random.random() < 0.3:
            x, y = hit_block.center
            kind = random.choice(POWERUP_TYPES)
            powerups.append({'rect': pygame.Rect(x, y, powerup_size, powerup_size), 'type': kind})

    # Power-up movement
    for p in powerups[:]:
        p['rect'].move_ip(0, 3)
        if p['rect'].colliderect(paddle):
            if p['type'] == 'extend':
                paddle.width = min(paddle.width + 30, WIDTH)
            elif p['type'] == 'slow':
                base_speed = max(base_speed - 1, 2)
            elif p['type'] == 'score':
                score += 50
            powerups.remove(p)
        elif p['rect'].top > HEIGHT:
            powerups.remove(p)

    # Game over
    if ball.bottom >= HEIGHT:
        ball.center = (WIDTH//2, HEIGHT//2)
        base_speed = 4
        ball_speed = [base_speed, -base_speed]
        score = 0
        paddle.width = 120
        blocks = [pygame.Rect(col * block_width, row * block_height, block_width - 2, block_height - 2)
                  for row in range(block_rows) for col in range(block_cols)]
        powerups.clear()

    # Draw everything
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    for p in powerups:
        color = GREEN if p['type'] == 'extend' else BLUE if p['type'] == 'slow' else YELLOW
        pygame.draw.rect(screen, color, p['rect'])

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)
import pygame
import random
import sys

pygame.init()

# Screen size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch The Ball")

clock = pygame.time.Clock()

# Player (basket)
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 8

# Ball
ball_radius = 15
ball_x = random.randint(20, WIDTH - 20)
ball_y = 0
ball_speed = 5

# Score & level
score = 0
level = 1
font = pygame.font.SysFont("Arial", 30)

running = True
game_over = False

# 🔁 MAIN GAME LOOP
while running:
    screen.fill((30, 30, 30))

    # ✅ EVENT HANDLING (VERY IMPORTANT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    if not game_over:
        # Ball falling
        ball_y += ball_speed

        # Collision detection
        if (ball_y + ball_radius >= player_y and
            player_x < ball_x < player_x + player_width):

            score += 1
            ball_y = 0
            ball_x = random.randint(20, WIDTH - 20)

            if score % 5 == 0:
                level += 1
                ball_speed += 1

        # Game over condition
        if ball_y > HEIGHT:
            game_over = True

    # Draw player
    pygame.draw.rect(
        screen,
        (0, 200, 0),
        (player_x, player_y, player_width, player_height)
    )

    # Draw ball
    pygame.draw.circle(
        screen,
        (200, 0, 0),
        (ball_x, ball_y),
        ball_radius
    )

    # Display score & level
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    # Game over screen
    if game_over:
        text = font.render(
            "Game Over! Press R = Restart | Q = Quit",
            True,
            (255, 0, 0)
        )
        screen.blit(text, (150, 300))

        if keys[pygame.K_r]:
            score = 0
            level = 1
            ball_speed = 5
            ball_y = 0
            game_over = False

        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

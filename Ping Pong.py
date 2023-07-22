import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the initial positions and velocities of the paddles and ball
paddle_width, paddle_height = 10, 60
paddle_speed = 5
player1_pos = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
player2_pos = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball_pos = pygame.Rect(width // 2 - 10, height // 2 - 10, 20, 20)
ball_velocity = pygame.Vector2(-9, 1)

# Initialize the scores
score_player1 = 0
score_player2 = 0

# Function to move the bot paddle
def move_bot_paddle():
    if ball_pos.y < player2_pos.y:
        player2_pos.y -= paddle_speed
    if ball_pos.y > player2_pos.y + paddle_height:
        player2_pos.y += paddle_speed

# Function to reset the ball position and velocity
def reset_ball():
    ball_pos.center = (width // 2, height // 2)
    ball_velocity.x *= random.choice([-1, 1])
    ball_velocity.y *= random.choice([-1, 1])

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos.y > 0:
        player1_pos.y -= paddle_speed
    if keys[pygame.K_s] and player1_pos.y < height - paddle_height:
        player1_pos.y += paddle_speed

    # Move the bot paddle
    move_bot_paddle()

    # Move the ball
    ball_pos.x += ball_velocity.x
    ball_pos.y += ball_velocity.y

    # Check for collision with the paddles
    if ball_pos.colliderect(player1_pos) or ball_pos.colliderect(player2_pos):
        ball_velocity.x *= -1

    # Check for collision with the walls
    if ball_pos.y > height - 20 or ball_pos.y < 0:
        ball_velocity.y *= -1

    # Check if the ball crosses the goals
    if ball_pos.x > width:
        score_player1 += 1
        reset_ball()
    elif ball_pos.x < 0:
        score_player2 += 1
        reset_ball()

    # Update the display
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1_pos)
    pygame.draw.rect(screen, WHITE, player2_pos)
    pygame.draw.ellipse(screen, WHITE, ball_pos)
    pygame.draw.aaline(screen, WHITE, (width // 2, 0), (width // 2, height))

    # Render the scores
    font = pygame.font.Font(None, 36)
    score_text1 = font.render(str(score_player1), True, WHITE)
    score_text2 = font.render(str(score_player2), True, WHITE)
    screen.blit(score_text1, (width // 4, 10))
    screen.blit(score_text2, (width // 4 * 3, 10))

    # Update the display
    pygame.display.flip()

    # Set the speed of the game
    clock.tick(60)

# Quit Pygame
pygame.quit()

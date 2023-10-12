import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Draw the snake on the screen
def draw_snake(screen, snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, WHITE, (*segment, 10, 10))

# Draw the food on the screen
def draw_food(screen, food_position):
    pygame.draw.rect(screen, WHITE, (*food_position, 10, 10))

# Display the player's score on the screen
def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Display a game over message on the screen
def show_game_over_message(screen, width, height):
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
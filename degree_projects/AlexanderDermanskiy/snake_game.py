import pygame
import sys
from snake import Snake
from food import Food
from collision import check_wall_collision, check_self_collision
from score import Score
from graphics import draw_snake, draw_food, draw_score, show_game_over_message

# Initialize Pygame
pygame.init()

# Constants
width = 640
height = 480
snake_speed = 15

# Set up the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)

# Create game objects
snake = Snake(width // 2, height // 2)
food = Food(width, height)
score = Score()

# Main game loop
is_game_over = False
while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    # Update game state
    snake.move()
    if check_wall_collision(snake.get_head_position(), width, height) or check_self_collision(snake.get_body()):
        is_game_over = True

    if snake.get_head_position() == food.get_position():
        snake.set_should_grow(True)  # Set the snake to grow
        food.respawn()
        score.increase_score()

    # Clear the screen
    screen.fill(black)

    # Draw game elements
    draw_snake(screen, snake.get_body())
    draw_food(screen, food.get_position())
    draw_score(screen, score.get_score())

    # Update the display
    pygame.display.update()

    # Control the game speed
    pygame.time.Clock().tick(snake_speed)

# Display game over message
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    show_game_over_message(screen, width, height)
    pygame.display.update()
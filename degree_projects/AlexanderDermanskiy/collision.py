# Check if the snake's head has collided with the game walls
def check_wall_collision(snake_head, width, height):
    head_x, head_y = snake_head
    if (
        head_x < 0 or head_x >= width or
        head_y < 0 or head_y >= height
    ):
        return True
    return False

# Check if the snake's head has collided with its own body
def check_self_collision(snake_body):
    head = snake_body[0]
    if head in snake_body[1:]:
        return True
    return False
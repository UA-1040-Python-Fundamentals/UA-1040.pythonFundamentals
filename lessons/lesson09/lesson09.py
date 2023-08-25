import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()
WHITE = (0, 0, 0)
# Loop until the user clicks the close button.
run = True
i = 0
cub = [100, 100]
KEYDOWN = False
# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    color = (int(i/(255*255))%255,
                       (int(i/255))%255,
                       i%255)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            run = False
        elif event.type == pygame.KEYDOWN:
            KEYDOWN = True
            if event.scancode == 82:
                cub[1] -=10
            if event.scancode == 79:
                cub[0] +=10

            if event.scancode == 81:
                cub[1] +=10

            if event.scancode == 80:
                cub[0] -=10

            print("User pressed a key.")
            print(event)
        elif event.type == pygame.KEYUP:
            KEYDOWN = False
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # x, y = event.pos
            # print(color)
            # if event.button == 1:
            #     pygame.draw.rect(gameDisplay, color, [x, y, x + 20, y + 25])
            # elif event.button == 3:
            #     pygame.draw.circle(gameDisplay, color, (x, y), 20)
            print("User pressed a mouse button")
            print(event)
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # print(i, color)
    gameDisplay.fill((10,10,10))
    pygame.draw.rect(gameDisplay, color, [cub[0], cub[1], 10, 10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    i += 3000
    clock.tick(60)

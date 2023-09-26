import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    new_x = COORD_X
    new_y = COORD_Y

    if keys[pygame.K_LEFT]:
        new_x -= DELTA_STEP
    if keys[pygame.K_RIGHT]:
        new_x += DELTA_STEP
    if keys[pygame.K_UP]:
        new_y -= DELTA_STEP
    if keys[pygame.K_DOWN]:
        new_y += DELTA_STEP

    if 0 <= new_x <= WIDTH_DISPLAY - WIDTH_RECTANGLE:
        COORD_X = new_x
    if 0 <= new_y <= HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        COORD_Y = new_y

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)

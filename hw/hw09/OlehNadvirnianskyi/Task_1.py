# Task 1
import pygame
from random import randint


def find_number():
    disp_width = 1200
    disp_height = 800

    gameDisplay = pygame.display.set_mode((disp_width, disp_height))

    pygame.display.set_caption("Task1:")

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 25)

    img = pygame.image.load(
        "D:\Git Projects\\UA-1040.pythonFundamentals\\hw\\hw09\\OlehNadvirnianskyi\\backg.jpg").convert_alpha()
    img = pygame.transform.scale(img, (disp_width, disp_height))

    border_thickness = 8
    border_color = (255, 155, 0)

    # Output text surf
    rect_width = 400
    rect_height = 150
    text = '      Choose a number between 1 and 100'
    text_surface = font.render(text, True, (0, 0, 0))

    rect_text = pygame.Rect(((disp_width - rect_width) // 2) + border_thickness,
                            ((disp_height - rect_height) // 2) + border_thickness, rect_width - 2 * border_thickness,
                            rect_height - 2 * border_thickness)
    rect_x = ((disp_width - rect_width) // 2) + (rect_width - text_surface.get_width()) // 2
    rect_y = ((disp_height - rect_height) // 2) + (rect_height - text_surface.get_height()) // 2

    # input text surf
    input_rect_width = 350
    input_rect_height = 70

    user_font = pygame.font.Font(None, 24)
    input_text = ''
    user_text_surface = user_font.render(input_text, True, (0, 255, 0))

    input_text_rect = pygame.Rect(((disp_width - input_rect_width) // 2) + border_thickness,
                                  ((disp_height - input_rect_height) // 2) + border_thickness + 150,
                                  input_rect_width - 2 * border_thickness, input_rect_height - 2 * border_thickness)
    input_text_x = ((disp_width - input_rect_width) // 2) + (input_rect_width - user_text_surface.get_width()) // 2
    input_text_y = (((disp_height - input_rect_height) // 2) + (
            input_rect_height - user_text_surface.get_height()) // 2) + 150

    number = randint(1, 100)
    attempts = 10

    run = True
    action = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_text_rect.collidepoint(event.pos):
                    action = True
                else:
                    action = False
            if event.type == pygame.KEYDOWN:
                if action == True:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        if attempts != 0:
                            try:
                                user_guess = float(input_text)
                                if user_guess == number:
                                    output = "You win!"
                                    text_surface = font.render(output, True, (0, 0, 0))
                                    input_text = ''

                                elif user_guess < number:
                                    output = f"Your number is too small. Attempts left: {attempts}"
                                    text_surface = font.render(output, True, (0, 0, 0))
                                    input_text = ''
                                    attempts -= 1
                                elif user_guess > number:
                                    output = f"Your number is too big. Attempts left: {attempts}"
                                    text_surface = font.render(output, True, (0, 0, 0))
                                    input_text = ''
                                    attempts -= 1
                            except ValueError:
                                output = "Enter the correct value"
                                text_surface = font.render(output, True, (0, 0, 0))
                                input_text = ''
                        elif attempts == 0:
                            output = "Your attempts is over"
                            text_surface = font.render(output, True, (0, 0, 0))
                            input_text = ''
        user_text_surface = user_font.render(input_text, True, (0, 0, 0))
        # background blit
        gameDisplay.blit(img, (0, 0))
        # output surface
        pygame.draw.rect(gameDisplay, border_color, ((disp_width - rect_width) // 2, (disp_height - rect_height) // 2,
                                                     rect_width, rect_height), border_thickness)
        pygame.draw.rect(gameDisplay, (0, 255, 0), rect_text)
        gameDisplay.blit(text_surface, (rect_x - 53, rect_y))
        # input surface
        pygame.draw.rect(gameDisplay, border_color, (
            (disp_width - rect_width) // 2, ((disp_height - rect_height) // 2) + 120, rect_width, rect_height),
                         border_thickness)
        pygame.draw.rect(gameDisplay, (255, 255, 255), input_text_rect)
        gameDisplay.blit(user_text_surface, (input_text_x - 15, input_text_y))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    find_number()
    pygame.quit()

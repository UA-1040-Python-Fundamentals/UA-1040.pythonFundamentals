import pygame
from random import randint


def main():

    display_width = 800
    display_height = 600

    GameDispaly = pygame.display.set_mode((display_width,display_height))

    pygame.display.set_caption("Guess the number")

    clock = pygame.time.Clock()

    img = pygame.image.load("hw09\\Alexander0108\\background.jpg").convert_alpha()
    img = pygame.transform.scale(img, (display_width,display_height))

    font = pygame.font.Font(None, 18)

    border_thickness = 5
    border_color = (0,0,0)

    #---------------------------------- Output Text Surface ----------------------
    rect_width = 400
    rect_height = 120
    text = 'Try to guess a number between 1 and 100'
    text_surface = font.render(text, True, (0,0,0))

    text_rect = pygame.Rect(((display_width-rect_width)//2)+border_thickness, ((display_height-rect_height)//2)+border_thickness, rect_width - 2 * border_thickness, rect_height - 2 * border_thickness)
    text_x = ((display_width-rect_width) // 2) + (rect_width - text_surface.get_width()) // 2
    text_y = ((display_height-rect_height) // 2) + (rect_height - text_surface.get_height()) // 2

    #---------------------------------- Input Text Surface -----------------------
    input_rect_width = 200
    input_rect_height = 80

    user_font = pygame.font.Font(None, 24)
    user_text = ''
    user_text_surface = user_font.render(user_text, True, (0,0,0))

    input_text_rect = pygame.Rect(((display_width-input_rect_width)//2)+border_thickness, ((display_height-input_rect_height)//2)+border_thickness+150, input_rect_width - 2 * border_thickness, input_rect_height - 2 * border_thickness)
    input_text_x = ((display_width-input_rect_width) // 2) + (input_rect_width - user_text_surface.get_width()) // 2
    input_text_y = (((display_height-input_rect_height) // 2) + (input_rect_height - user_text_surface.get_height()) // 2) + 150


    active = True
    input_active = False

    number = randint(1,100)
    attempts = 10

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_text_rect.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN:
                if input_active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        if attempts != 0:
                            try:
                                user_number = float(user_text)
                                if user_number == number:
                                    text = 'Congratulation! You win!'
                                    text_surface = font.render(text, True, (0,0,0))
                                    user_text = '' 
                                elif user_number < number:
                                    text = f'Your number is less than the given number. Attempts left: {attempts}'
                                    text_surface = font.render(text, True, (0,0,0))
                                    user_text = ''
                                    attempts -= 1
                                else:
                                    text = f'Your number is bigger than the given number. Attempts left: {attempts}'
                                    text_surface = font.render(text, True, (0,0,0))
                                    user_text = ''
                                    attempts -= 1                                              
                            except ValueError:
                                text = 'Enter the correct value'
                                text_surface = font.render(text, True, (0,0,0))
                                user_text = ''
                        elif attempts == 0:
                            text = 'Unfortunately, your attempts have come to an end :('
                            text_surface = font.render(text, True, (0,0,0))
                            user_text = ''                            

                        
        user_text_surface = user_font.render(user_text, True, (0,0,0))

        #---------------------------------- Blit (insert) the background image --------------------------------------
        GameDispaly.blit(img, (0,0))

        #--------------------------- Draw output text Surface / his border and blit it ------------------------------
        pygame.draw.rect(GameDispaly, border_color, ((display_width-rect_width)//2, (display_height-rect_height)//2, rect_width, rect_height), border_thickness)
        pygame.draw.rect(GameDispaly, (255,255,255), text_rect)
        GameDispaly.blit(text_surface, (text_x-53, text_y))

        #--------------------------- Draw input text Surface / his border and blit it -------------------------------
        pygame.draw.rect(GameDispaly, border_color, ((display_width-input_rect_width)//2, ((display_height-input_rect_height)//2)+150, input_rect_width, input_rect_height), border_thickness)
        pygame.draw.rect(GameDispaly, (255,255,255), input_text_rect)
        GameDispaly.blit(user_text_surface, (input_text_x-12, input_text_y))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
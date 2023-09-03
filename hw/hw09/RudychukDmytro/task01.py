import pygame
import random


message = ""


pygame.init()


WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")


font = pygame.font.Font(None, 36)


target_number = random.randint(1, 100)


attempts = 10
guessed = False
input_number = ""

running = True
while running:
    screen.fill(WHITE)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(input_number)
                    if guess < target_number:
                        message = "Go higher!"
                    elif guess > target_number:
                        message = "Go lower!"
                    else:
                        message = f"Congratulations! You guessed it: {target_number}"
                        guessed = True
                except ValueError:
                    message = "Invalid input. Enter a number."
                attempts -= 1
                input_number = ""
            elif event.key == pygame.K_BACKSPACE:
                input_number = input_number[:-1]
            else:
                input_number += event.unicode


    attempts_text = font.render(f"Attempts left: {attempts}", True, BLACK)
    input_text = font.render(input_number, True, BLACK)

    screen.blit(attempts_text, (20, 20))
    screen.blit(input_text, (20, 70))


    hint_text = font.render(message, True, BLACK)
    screen.blit(hint_text, (20, 150))


    if attempts == 0 and not guessed:
        message = f"You ran out of attempts. The number was {target_number}"
        hint_text = font.render(message, True, BLACK)
        screen.blit(hint_text, (20, 150))

    pygame.display.flip()


pygame.quit()

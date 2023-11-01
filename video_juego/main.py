import pygame
from pygame.locals import *

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up player input
name_input = ''
name_input_rect = pygame.Rect(250, 400, 300, 50)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

running = True
while running:
    screen.fill(WHITE)
    draw_text('Cruz puto', font, BLUE, 150, 200)
    draw_text('Press the mouse button to start playing', font, BLUE, 250, 300)
    draw_text('Enter your name:', font, BLUE, 250, 400)
    draw_text(name_input, font, BLUE, 550, 400)
    
    pygame.draw.rect(screen, BLUE, name_input_rect, 2)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                name_input = name_input[:-1]
            else:
                name_input += event.unicode

        if event.type == MOUSEBUTTONDOWN:
            # Proceed to the game
            print(f'Player name is: {name_input}')
            running = False

    pygame.display.flip()

pygame.quit()
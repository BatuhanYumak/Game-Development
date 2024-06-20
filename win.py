import pygame
from sys import exit

def show_win_screen(window, win_image, win_width, win_height):
    window.fill((0, 0, 0))
    window.blit(win_image, (win_width // 2 - win_image.get_width() // 2, win_height // 2 - win_image.get_height() // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

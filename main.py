import pygame
from sys import exit
import sys


pygame.init()
clock = pygame.time.Clock()

# Screen
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))


# Assets
bird_images = [
    pygame.image.load("assets/bird_down.png"),
    pygame.image.load("assets/bird_mid.png"),
    pygame.image.load("assets/bird_up.png"),
]

skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

# Game
scroll_speed = 1
bird_start_position = (100,250)

# class Bird(pygame.sprite.Sprite):
#         def __init__(self):
#             pygame.sprite.Sprite.__init__(self)
#             self.image = bird_images[0]
#             self.


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()


def update(self):
    self.rect.x -= scroll_speed
    if self.rect.right < 0:
        self.rect.left = win_width
        self.kill()


def quit_game():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Game run


def main():

    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))

    run = True
    quit_game()

    # Reset Frame
    window.fill((0, 0, 0))
    # Draw Background
    window.blit(skyline_image, (0, 0))

    # Spawn Ground
    if len(ground) < 2:
        ground.add(Ground(win_width, y_pos_ground))



    #Draw Pipes, Ground and Bird
    ground.draw(window)

    # Update Display
    ground.update

    clock.tick(60)
    pygame.display.update()


main()

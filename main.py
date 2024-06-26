import pygame
from sys import exit
import random

# Initialize pygame and clock for controlling the frame rate
pygame.init()
clock = pygame.time.Clock()

# Window dimensions
win_height = 720
win_width = 551
# Create game window
window = pygame.display.set_mode((win_width, win_height))

# Load images for game elements
bird_images = [
    pygame.image.load("assets/bird_down.png"),
    pygame.image.load("assets/bird_mid.png"),
    pygame.image.load("assets/bird_up.png"),
]

rip_image = pygame.image.load("assets/rip.png")
blauwe_vogel = pygame.image.load("assets/blauwe_vogel.png")
groene_vogel = pygame.image.load("assets/groene_vogel.png")
gele_vogel = pygame.image.load("assets/gele_vogel.png")
logo_image = pygame.image.load("assets/logo_zonder_tekst.png")
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

logo_width = 100
logo_height = 100
logo_img = pygame.transform.scale(logo_image, (logo_width, logo_height))
gele_vogel = pygame.transform.scale(gele_vogel, (60, 60))
groene_vogel = pygame.transform.scale(groene_vogel, (45, 45))
rip_image = pygame.transform.scale(rip_image, (60, 60))

# background sound
pygame.mixer.music.load("assets/achtergrond.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# point sound
point_sound = pygame.mixer.Sound("assets/point.mp3")


# Game settings
scroll_speed = 1
bird_start_position = (100, 250)
score = 0
font = pygame.font.SysFont("Segoe", 26)
game_stopped = True

# Bird class representing the player's character
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True

    def update(self, user_input):
        # Animate Bird by cycling through images
        if self.alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0

        # Change bird color after reaching 5 points
        if score >= 5:
            self.image = gele_vogel
            if score >= 10:
                self.image = groene_vogel
                if score >= 15:
                    self.image = blauwe_vogel
        else:
            self.image = bird_images[self.image_index // 10]

        # Apply gravity and check for flap action
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        # Rotate Bird based on velocity
        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        # Handle user input for bird flap
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7

# Pipe class for the obstacles
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.pipe_type = pipe_type

    def update(self):
        # Move Pipe leftwards
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()


# Logo class for the collectible items
class Logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = logo_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move logo leftwards
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()


# Ground class for the scrolling ground
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground leftwards
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()

# Function to handle quitting the game
def quit_game():
    # Exit Game if quit event is detected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Main game loop
def main():
    global score

    # Create a bird instance
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    # Pipe setup
    pipe_timer = 0
    pipes = pygame.sprite.Group()
    logos = pygame.sprite.Group()

    # Initial ground setup
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))

    run = True
    while run:
        # Handle quit events
        quit_game()

        # Clear screen for next frame
        window.fill((0, 0, 0))

        # Get user input
        user_input = pygame.key.get_pressed()

        # Draw background
        window.blit(skyline_image, (0, 0))

        # Add ground sections as needed
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground))

        # Draw pipes, logos, ground, and bird
        pipes.draw(window)
        logos.draw(window)
        ground.draw(window)
        bird.draw(window)

        # Display the score
        score_text = font.render("Score: " + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20))

        # Update pipes, logos, ground, and bird if bird is alive
        if bird.sprite.alive:
            pipes.update()
            logos.update()
            ground.update()
        bird.update(user_input)

        # Check for collisions with pipes and ground
        collision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
        collision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if collision_pipes or collision_ground:
            bird.sprite.alive = False
            if collision_ground:
                # Display game over screen
                window.blit(game_over_image, (win_width // 2 - game_over_image.get_width() // 2, win_height // 2 - game_over_image.get_height() // 2))
                window.blit(
                    rip_image,
                    (
                        win_width // 2 - rip_image.get_width() // 2,
                        win_height // 2 - game_over_image.get_height() // 2 + -100,
                    ),
                )
                if user_input[pygame.K_r]:
                    score = 0
                    break

        # Check for collisions with logos
        collision_logos = pygame.sprite.spritecollide(bird.sprites()[0], logos, True)
        if collision_logos:
            score += 1
            point_sound.play()

        # Spawn new pipes and logos periodically
        if pipe_timer <= 0 and bird.sprite.alive:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image, 'top'))
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom'))
            logo_y = (
                y_top
                + top_pipe_image.get_height()
                + (y_bottom - y_top - top_pipe_image.get_height()) // 2
                - logo_height // 2
            )
            logos.add(Logo(x_bottom, logo_y))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1

        # Control the frame rate
        clock.tick(60)
        pygame.display.flip()

# Menu loop to start the game
def menu():
    global game_stopped

    while game_stopped:
        quit_game()

        # Draw initial menu screen
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, 0))
        window.blit(ground_image, Ground(0, 520))
        window.blit(bird_images[0], (100, 250))
        window.blit(start_image, (win_width // 2 - start_image.get_width() // 2, win_height // 2 - start_image.get_height() // 2))

        # Start game if space is pressed
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()

# Start the menu
menu()

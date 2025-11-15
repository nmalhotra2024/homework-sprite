import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites With Custom Event")

clock = pygame.time.Clock()

# -----------------------------
# Custom Event for color change
# -----------------------------
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 1000)   # trigger every 1 second


# -----------------------------
# Sprite Class
# -----------------------------
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        # Randomize color
        self.color = (random.randint(0,255),
                      random.randint(0,255),
                      random.randint(0,255))
        self.image.fill(self.color)


# -----------------------------
# Create two sprites
# -----------------------------
sprite1 = ColorSprite(200, HEIGHT // 2, (255, 0, 0))   # Red
sprite2 = ColorSprite(400, HEIGHT // 2, (0, 0, 255))   # Blue

sprite_group = pygame.sprite.Group(sprite1, sprite2)


# -----------------------------
# Game loop
# -----------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle custom color-change event
        if event.type == COLOR_CHANGE_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Drawing
    screen.fill((30, 30, 30))
    sprite_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

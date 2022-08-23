import time
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FIREWORK_COLORS = [
    (176, 177, 223),
    (2, 126, 139),
    (126, 78, 176),
    (220, 237, 129),
    (210, 14, 8),
    (67, 211, 155),
    (245, 88, 95),
    (231, 137, 144),
    (0, 126, 180),
    (195, 254, 21),
]


class Shooters:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw_shooters(self, width, height, color, size, screen):
        for pixel in range(1, size[0]):
            if pixel % (size[0] // 4) == 0:
                print(pixel)
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(pixel, size[1] - height, width, height),
                )


pygame.init()

# Set the width and height of the screen [width, height]
size = (600, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Fireworks")

done = False

clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    shooters = Shooters(15, 15, WHITE)
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    shooters.draw_shooters(15, 15, WHITE, size, screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

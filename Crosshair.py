import pygame
from Sprite import Sprite


class Crosshair(Sprite):
    def __init__(self, x, y, img, width=None, height=None):
        super().__init__(x, y, img, width, height)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        # pygame.mouse.set_visible(False)

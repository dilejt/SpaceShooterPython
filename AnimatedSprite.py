import pygame

from Sprite import Sprite
from helpers import getStrips


class AnimatedSprite(Sprite):
    def __init__(self, x, y, strips_dict, width=None, height=None, infinite=False):
        super().__init__(x, y, None)
        self.strips = getStrips(strips_dict)
        self.current = 0
        self.is_animating = infinite
        self.infinite = infinite
        self.width = width
        self.height = height
        if width is not None and height is not None:
            self.image = pygame.transform.scale(self.strips[self.current], (width, height))
        else:
            self.image = self.strips[self.current]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def animate(self):
        self.is_animating = True

    def update(self, animation_speed=1):
        if self.is_animating:
            self.current += (1 / animation_speed)
            if self.current >= len(self.strips):
                if self.infinite:
                    self.current = 0
                else:
                    self.is_animating = False
                    self.kill()
                    return
            if self.width is not None and self.height is not None:
                self.image = pygame.transform.scale(self.strips[int(self.current)], (self.width, self.height))
            else:
                self.image = self.strips[int(self.current)]


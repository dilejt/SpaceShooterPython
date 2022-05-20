from Sprite import Sprite
from helpers import getStrips


class AnimatedSprite(Sprite):
    def __init__(self, x, y, strips_dict, infinite=False):
        super().__init__(x, y, None)
        self.strips = getStrips(strips_dict)
        self.current = 0
        self.is_animating = infinite
        self.infinite = infinite
        self.animation_speed_ratio = 5
        self.image = self.strips[self.current]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def animate(self):
        self.is_animating = True

    def update(self, animation_speed=None):
        if self.is_animating:
            if animation_speed is None:
                self.current += 1 / self.animation_speed_ratio
            else:
                self.current += 1 / animation_speed
            if self.infinite and self.current >= len(self.strips):
                self.current = 0
                if not self.infinite:
                    self.is_animating = False
            self.image = self.strips[int(self.current)]

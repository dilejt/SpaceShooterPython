from AnimatedSprite import AnimatedSprite


class Explosion(AnimatedSprite):
    def __init__(self, x, y, width):
        super().__init__(x, y, 'explosion', width, width)
        self.rect.center = [x, y]

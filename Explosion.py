from AnimatedSprite import AnimatedSprite


class Explosion(AnimatedSprite):
    explosion_width = 120
    explosion_height = 120

    def __init__(self, x, y):
        super().__init__(x, y, 'explosion', self.explosion_width, self.explosion_height)
        self.rect.center = [x, y]

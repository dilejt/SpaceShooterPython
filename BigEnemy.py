import random

from Sprite import Sprite
from consts import SCREEN_WIDTH, SCREEN_HEIGHT


class BigEnemy(Sprite):
    big_enemy_width = 100
    big_enemy_height = 134

    def __init__(self):
        super().__init__(random.randint(0, SCREEN_WIDTH - self.big_enemy_width), -self.big_enemy_height, 'enemy_big.png',
                         self.big_enemy_width, self.big_enemy_height)
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT + self.big_enemy_height:
            self.kill()

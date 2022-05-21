import random

from Sprite import Sprite
from consts import SCREEN_WIDTH, SCREEN_HEIGHT


def spawnBigEnemy(elapsed_time, big_enemies_layer):
    if elapsed_time > BigEnemy.spawn_timer_handler:
        BigEnemy.spawn_rate = random.randint(3000, 6000)
        BigEnemy.spawn_timer_handler += BigEnemy.spawn_rate
        big_enemies_layer.add(BigEnemy())
    big_enemies_layer.update()


class BigEnemy(Sprite):
    big_enemy_width = 100
    big_enemy_height = 134
    spawn_rate = random.randint(1000, 3000)
    spawn_timer_handler = spawn_rate

    def __init__(self):
        super().__init__(random.randint(0, SCREEN_WIDTH - self.big_enemy_width), -self.big_enemy_height, 'enemy_big.png',
                         self.big_enemy_width, self.big_enemy_height)
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT + self.big_enemy_height:
            self.kill()

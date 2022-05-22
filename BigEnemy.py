import random

from HealthBar import HealthBar
from Sprite import Sprite
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, GUI_HEIGHT


def spawnBigEnemy(elapsed_time, big_enemies_layer, player, hp_bar):
    if elapsed_time > BigEnemy.spawn_timer_handler:
        BigEnemy.spawn_rate = random.randint(3000, 6000)
        BigEnemy.spawn_timer_handler += BigEnemy.spawn_rate
        big_enemies_layer.add(BigEnemy(player, hp_bar))
    big_enemies_layer.update()


class BigEnemy(Sprite):
    big_enemy_width = 100
    big_enemy_height = 134
    spawn_rate = random.randint(1000, 3000)
    spawn_timer_handler = spawn_rate

    def __init__(self, player, hp_bar):
        super().__init__(random.randint(0, SCREEN_WIDTH - self.big_enemy_width), -self.big_enemy_height + 5, 'enemy_big.png',
                         self.big_enemy_width, self.big_enemy_height)
        self.speed = 1
        self.player = player
        self.hp_bar = hp_bar

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT - GUI_HEIGHT:
            self.kill()
            self.hp_bar.hp_diff += -5

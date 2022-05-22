import random

from Sprite import Sprite
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, GUI_HEIGHT


def spawnSmallEnemy(elapsed_time, big_enemies_layer, player, hp_bar):
    if elapsed_time > SmallEnemy.spawn_timer_handler:
        SmallEnemy.spawn_rate = random.randint(2000, 4000)
        SmallEnemy.spawn_timer_handler += SmallEnemy.spawn_rate
        big_enemies_layer.add(SmallEnemy(player, hp_bar))
    big_enemies_layer.update()


class SmallEnemy(Sprite):
    small_enemy_width = 80
    small_enemy_height = 80
    spawn_rate = random.randint(0, 1000)
    spawn_timer_handler = spawn_rate

    def __init__(self, player, hp_bar):
        super().__init__(random.randint(0, SCREEN_WIDTH - self.small_enemy_width), -self.small_enemy_height + 5, 'enemy_small.png',
                         self.small_enemy_width, self.small_enemy_height)
        self.speed = 2
        self.player = player
        self.hp_bar = hp_bar

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT - GUI_HEIGHT:
            self.kill()
            self.hp_bar.hp_diff += -5

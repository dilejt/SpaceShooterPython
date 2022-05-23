import pygame

from AnimatedSprite import AnimatedSprite
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, INIT_HP


class HealthBar(AnimatedSprite):
    health_bar_width = 216
    health_bar_height = 58

    def __init__(self, player):
        super().__init__(SCREEN_WIDTH - self.health_bar_width - 5, SCREEN_HEIGHT - self.health_bar_height - 5, 'hp', self.health_bar_width,
                         self.health_bar_height)
        self.hp_diff = 0
        self.player = player
        self.current = player.hp
        self.image = pygame.transform.scale(self.strips[player.hp], (self.width, self.height))

    def update(self, animation_speed=8):
        if self.hp_diff != 0:
            if self.hp_diff < 0:
                self.hp_diff += (1 / animation_speed)
                self.current -= (1 / animation_speed)
            elif self.hp_diff > 0:
                if self.player.hp >= INIT_HP:
                    self.hp_diff = 0
                    return
                self.hp_diff -= (1 / animation_speed)
                self.current += (1 / animation_speed)
            self.player.hp = int(self.current)
        else:
            return
        if self.current >= len(self.strips):
            return
        elif self.current < 0:
            return
        self.image = pygame.transform.scale(self.strips[int(self.current)], (self.width, self.height))

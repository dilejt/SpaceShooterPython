import random

from AnimatedSprite import AnimatedSprite
from consts import SCREEN_HEIGHT, GUI_HEIGHT, SCREEN_WIDTH


def spawnFirstAid(elapsed_time, first_aid):
    if elapsed_time > FirstAid.spawn_timer_handler:
        FirstAid.spawn_rate = random.randint(4000, 6000)
        FirstAid.spawn_timer_handler += FirstAid.spawn_rate
        first_aid.add(FirstAid())
    first_aid.update()


class FirstAid(AnimatedSprite):
    first_aid_width = 40
    first_aid_height = 40
    spawn_rate = random.randint(1000, 3000)
    spawn_timer_handler = spawn_rate

    def __init__(self):
        super().__init__(random.randint(0, SCREEN_WIDTH - self.first_aid_width), -self.first_aid_height + 5, 'first_aid', self.first_aid_width,
                         self.first_aid_height, True)
        self.speed = 3.5
        self.current = random.randint(0, len(self.strips) - 1)

    def update(self, animation_speed=4):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT - GUI_HEIGHT:
            self.kill()
        else:
            AnimatedSprite.update(self, animation_speed)

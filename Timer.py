import pygame

from Sprite import Sprite
from consts import SCREEN_HEIGHT, GUI_HEIGHT


class Timer(Sprite):
    def __init__(self):
        super().__init__(0, 0, None)
        self.font = pygame.font.Font("assets/fonts/DS-DIGIB.ttf", 30)

    def update(self, time, screen):
        timer_font = self.font.render("Time: " + (str(time)[:-3] if str(time)[:-3] else "0") + "." + str(time)[-3:-1], True, (255, 255, 255))
        screen.blit(timer_font, (10, SCREEN_HEIGHT - GUI_HEIGHT + 5))

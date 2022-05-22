import pygame

from Sprite import Sprite
from consts import SCREEN_HEIGHT, GUI_HEIGHT


class Score(Sprite):
    def __init__(self):
        super().__init__(0, 0, None)
        self.font = pygame.font.Font("assets/fonts/DS-DIGIB.ttf", 30)
        self.points = 0

    def update(self, screen):
        score_font = self.font.render("SCORE: " + str(self.points), True, (255, 255, 255))
        screen.blit(score_font, (10, SCREEN_HEIGHT - GUI_HEIGHT + 35))

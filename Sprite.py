import pygame

from consts import SCREEN_WIDTH, SCREEN_HEIGHT


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, img, width=None, height=None, sound_path=None):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 3
        self.moveUp = False
        self.moveDown = False
        self.moveRight = False
        self.moveLeft = False
        if img is not None:
            self.image = pygame.image.load(img)
            if width is not None or height is not None:
                self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect()
            self.rect.topleft = [x, y]
        if sound_path is not None:
            self.sound = pygame.mixer.Sound(sound_path)

    def checkBorderCollision(self, x, y, difference):
        if self.x - difference < 0 and x is False:
            return True
        elif self.x + self.image.get_width() + difference > SCREEN_WIDTH and x is True:
            return True
        elif self.y - difference < 0 and y is False:
            return True
        elif self.y + self.image.get_height() + difference > SCREEN_HEIGHT and y is True:
            return True
        return False

import pygame

from consts import SCREEN_WIDTH, SCREEN_HEIGHT, GUI_HEIGHT


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, img, width=None, height=None, sound_file=None):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 3
        self.moveUp = False
        self.moveDown = False
        self.moveRight = False
        self.moveLeft = False
        if img is not None:
            if '.png' in img:
                self.image = pygame.image.load("assets/pictures/" + img).convert_alpha()
            else:
                self.image = pygame.image.load("assets/pictures/" + img)
            if width is not None and height is not None:
                self.image = pygame.transform.scale(self.image, (width, height))
            self.mask = pygame.mask.from_surface(self.image)
            self.outline = pygame.draw.lines(self.image, (200, 150, 150), True, self.mask.outline())
            # pygame.draw.rect(self.image, (255, 0, 0), [0, 0, width, height], 1)
            # all colored
            # pygame.draw.polygon(self.image, (pygame.Color(123, 123, 123, 128)), self.mask.outline(), 0)
            self.rect = self.image.get_rect()
            self.rect.topleft = [x, y]
        if sound_file is not None:
            self.sound = pygame.mixer.Sound("assets/sounds/" + sound_file)

    def checkBorderCollision(self, x, y, difference):
        if self.x - difference < 0 and x is False:
            return True
        elif self.x + self.image.get_width() + difference > SCREEN_WIDTH and x is True:
            return True
        elif self.y - difference < 0 and y is False:
            return True
        elif self.y + self.image.get_height() + difference > SCREEN_HEIGHT - GUI_HEIGHT and y is True:
            return True
        return False

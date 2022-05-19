import sys
import pygame
from os import listdir
from os.path import isfile, join


def getStrips(directory=''):
    return [pygame.image.load(directory + '/' + file) for file in [f for f in listdir(directory) if isfile(join(directory, f))]]


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, img, width=None, height=None, sound_path=None):
        super().__init__()
        self.screen_width = 800
        self.screen_height = 1000
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
            # self.sound.play()

    def movement(self):
        if self.moveUp and not self.checkBorderCollision(None, False):
            if self.moveLeft or self.moveRight:
                self.y -= (self.speed/3)
            else:
                self.y -= self.speed
        if self.moveDown and not self.checkBorderCollision(None, True):
            if self.moveLeft or self.moveRight:
                self.y += (self.speed/3)
            else:
                self.y += self.speed
        if self.moveRight and not self.checkBorderCollision(True, None):
            if self.moveUp or self.moveDown:
                self.x += (self.speed/3)
            else:
                self.x += self.speed
        if self.moveLeft and not self.checkBorderCollision(False, None):
            if self.moveUp or self.moveDown:
                self.x -= (self.speed/3)
            else:
                self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def checkBorderCollision(self, x, y):
        if self.x - self.speed < 0 and x is False:
            return True
        elif self.x + self.image.get_width() + self.speed > self.screen_width and x is True:
            return True
        elif self.y - self.speed < 0 and y is False:
            return True
        elif self.y + self.image.get_height() + self.speed > self.screen_height and y is True:
            return True
        return False


class AnimatedSprite(Sprite):
    def __init__(self, x, y, strips_dict, infinite=False):
        super().__init__(x, y, None)
        self.strips = getStrips(strips_dict)
        self.current = 0
        self.is_animating = infinite
        self.infinite = infinite
        self.animation_speed_ratio = 5
        self.image = self.strips[self.current]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def animate(self):
        self.is_animating = True

    def update(self, speed=None):
        if self.is_animating:
            if speed is None:
                self.current += 1 / self.animation_speed_ratio
            else:
                self.current += 1 / speed
            if self.infinite and self.current >= len(self.strips):
                self.current = 0
                if not self.infinite:
                    self.is_animating = False
            self.image = self.strips[int(self.current)]


class Crosshair(Sprite):
    def __init__(self, x, y, img, width=None, height=None):
        super().__init__(x, y, img, width, height)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        # pygame.mouse.set_visible(False)


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen_width = 800
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Space Shooter")

        self.bg_layer = pygame.sprite.Group()
        self.background = AnimatedSprite(0, 0, 'bg', True)
        self.bg_layer.add(self.background)

        self.top_layer = pygame.sprite.Group()
        self.player = Sprite(0, 0, 'player.png', 100, 100)
        self.top_layer.add(self.player)

        self.mainLoop()

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.KEYDOWN:
                #     # if event.key == pygame.K_ESCAPE:
                #     #     terminate()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.player.moveUp = False
                    if event.key == pygame.K_DOWN:
                        self.player.moveDown = False
                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft = False
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.player.moveUp = True
                self.player.moveDown = False
                self.player.movement()
            if keys[pygame.K_DOWN]:
                self.player.moveUp = False
                self.player.moveDown = True
                self.player.movement()
            if keys[pygame.K_LEFT]:
                self.player.moveRight = False
                self.player.moveLeft = True
                self.player.movement()
            if keys[pygame.K_RIGHT]:
                self.player.moveRight = True
                self.player.moveLeft = False
                self.player.movement()

                # rest events
            # rest code

            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            self.bg_layer.draw(self.screen)
            self.background.update()
            self.top_layer.draw(self.screen)
            self.clock.tick(60)

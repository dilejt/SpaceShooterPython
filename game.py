import sys
import pygame
from os import listdir
from os.path import isfile, join


def getStrips(directory=''):
    return [pygame.image.load(directory + '/' + file) for file in [f for f in listdir(directory) if isfile(join(directory, f))]]


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, img, width=None, height=None, sound_path=None):
        super().__init__()
        self.x = x
        self.y = y
        self.moveUp = True
        self.moveDown = False
        self.moveRight = False
        self.moveLeft = True
        if img is not None:
            self.image = pygame.image.load(img)
            if width is not None or height is not None:
                self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect()
            self.rect.topleft = [x, y]
        if sound_path is not None:
            self.sound = pygame.mixer.Sound(sound_path)
            # self.sound.play()


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
                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_ESCAPE:
                    #     terminate()
                    if event.key == pygame.K_UP:
                        self.player.moveUp = True
                        self.player.moveDown = False
                    if event.key == pygame.K_DOWN:
                        self.player.moveUp = False
                        self.player.moveDown = True
                    if event.key == pygame.K_LEFT:
                        self.player.moveRight = False
                        self.player.moveLeft = True
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight = True
                        self.player.moveLeft = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.player.moveUp = False
                    if event.key == pygame.K_DOWN:
                        self.player.moveDown = False
                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft = False
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight = False

                # rest events
            # rest code

            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            self.bg_layer.draw(self.screen)
            self.background.update()
            self.top_layer.draw(self.screen)
            self.clock.tick(60)

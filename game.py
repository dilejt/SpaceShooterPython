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

    def checkBorderCollision(self, x, y, difference):
        if self.x - difference < 0 and x is False:
            return True
        elif self.x + self.image.get_width() + difference > Game.screen_width and x is True:
            return True
        elif self.y - difference < 0 and y is False:
            return True
        elif self.y + self.image.get_height() + difference > Game.screen_height and y is True:
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

    def update(self, animation_speed=None):
        if self.is_animating:
            if animation_speed is None:
                self.current += 1 / self.animation_speed_ratio
            else:
                self.current += 1 / animation_speed
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


class Player(Sprite):
    player_width = 100
    player_height = 100

    def __init__(self):
        super().__init__(Game.screen_width / 2 - self.player_width / 2, Game.screen_height - self.player_height, 'player.png', self.player_width,
                         self.player_height)
        self.shooting_timer_multiplier = 0

    def movement(self):
        if self.moveUp and not self.checkBorderCollision(None, False, self.speed):
            if self.moveLeft or self.moveRight:
                self.y -= (self.speed / 3)
            else:
                self.y -= self.speed
        if self.moveDown and not self.checkBorderCollision(None, True, self.speed):
            if self.moveLeft or self.moveRight:
                self.y += (self.speed / 3)
            else:
                self.y += self.speed
        if self.moveRight and not self.checkBorderCollision(True, None, self.speed):
            if self.moveUp or self.moveDown:
                self.x += (self.speed / 3)
            else:
                self.x += self.speed
        if self.moveLeft and not self.checkBorderCollision(False, None, self.speed):
            if self.moveUp or self.moveDown:
                self.x -= (self.speed / 3)
            else:
                self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def shooting(self, elapsed_time, beam_layer, screen):
        if elapsed_time - 1000 * self.shooting_timer_multiplier > 1000:
            self.shooting_timer_multiplier += 1
            beam_layer.add(Beam(self))
        beam_layer.update()
        beam_layer.draw(screen)


class Beam(Sprite):
    def __init__(self, player):
        self.beam_width = 6
        self.beam_height = 50
        super().__init__(player.x + player.player_width / 2 - self.beam_width / 2, player.y - self.beam_height, 'beam.png', self.beam_width,
                         self.beam_height)
        self.speed = 12

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


class Game:
    screen_width = 800
    screen_height = 1000

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Space Shooter")

        self.bg_layer = pygame.sprite.Group()
        self.background = AnimatedSprite(0, 0, 'bg', True)
        self.bg_layer.add(self.background)

        self.player_layer = pygame.sprite.Group()
        self.player = Player()
        self.player_layer.add(self.player)

        self.beam_layer = pygame.sprite.Group()

        elapsed_time = 0
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
            dt = self.clock.tick(60)
            elapsed_time += dt

            pygame.display.flip()
            self.screen.fill((0, 0, 0))

            self.bg_layer.draw(self.screen)
            self.bg_layer.update()

            self.player_layer.draw(self.screen)
            self.player.shooting(elapsed_time, self.beam_layer, self.screen)

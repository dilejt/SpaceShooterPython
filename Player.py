import pygame.transform

from Beam import Beam
from Sprite import Sprite
from consts import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(Sprite):
    player_width = 80
    player_height = 80

    def __init__(self):
        super().__init__(SCREEN_WIDTH / 2 - self.player_width / 2, SCREEN_HEIGHT - self.player_height, 'player.png', self.player_width,
                         self.player_height)
        self.shooting_timer_multiplier = 0
        self.shooting_rate = 1000

    def movement(self):
        # transparent
        # self.image = pygame.transform.laplacian(self.image)
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
        if elapsed_time - self.shooting_rate * self.shooting_timer_multiplier > self.shooting_rate:
            self.shooting_timer_multiplier += 1
            beam_layer.add(Beam(self))
        beam_layer.update()
        beam_layer.draw(screen)

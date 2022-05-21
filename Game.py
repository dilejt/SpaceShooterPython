import sys
import pygame

from AnimatedSprite import AnimatedSprite
from BigEnemy import spawnBigEnemy
from Player import Player
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)

        self.bg_layer = pygame.sprite.Group()
        self.background = AnimatedSprite(0, 0, 'bg', True)
        self.bg_layer.add(self.background)

        self.player_layer = pygame.sprite.Group()
        self.player = Player()
        self.player_layer.add(self.player)

        self.beam_layer = pygame.sprite.Group()

        self.big_enemies_layer = pygame.sprite.Group()

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

            spawnBigEnemy(elapsed_time, self.beam_layer, self.screen)

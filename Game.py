import sys
import pygame

from AnimatedSprite import AnimatedSprite
from BigEnemy import spawnBigEnemy
from Explosion import Explosion
from Gui import Gui
from HealthBar import HealthBar
from Player import Player
from Score import Score
from SmallEnemy import spawnSmallEnemy
from Timer import Timer
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)

        self.bg_layer = pygame.sprite.GroupSingle()
        self.background = AnimatedSprite(0, 0, 'bg', None, None, True)
        self.bg_layer.add(self.background)

        self.player_layer = pygame.sprite.GroupSingle()
        self.player = Player()
        self.player_layer.add(self.player)

        self.beam_layer = pygame.sprite.Group()

        self.explosion_layer = pygame.sprite.Group()

        self.big_enemies_layer = pygame.sprite.Group()

        self.small_enemies_layer = pygame.sprite.Group()

        self.gui_layer = pygame.sprite.GroupSingle()
        self.gui = Gui()
        self.gui_layer.add(self.gui)

        self.hp_layer = pygame.sprite.GroupSingle()
        self.hp_bar = HealthBar(self.player)
        self.hp_layer.add(self.hp_bar)

        self.timer = Timer()
        self.score = Score()

        self.ADD_TIME_POINTS = pygame.USEREVENT + 41

        self.clock = pygame.time.Clock()
        elapsed_time = 0
        pygame.time.set_timer(self.ADD_TIME_POINTS, 1000)

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
                if event.type == self.ADD_TIME_POINTS:
                    self.score.points += 10

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

            dt = self.clock.tick(60)
            elapsed_time += dt

            pygame.display.flip()
            self.screen.fill((0, 0, 0))

            self.bg_layer.draw(self.screen)
            self.bg_layer.update(4)

            self.player_layer.draw(self.screen)
            self.player.shooting(elapsed_time, self.beam_layer, self.screen)

            self.big_enemies_layer.draw(self.screen)
            spawnBigEnemy(elapsed_time, self.big_enemies_layer, self.player, self.hp_bar)

            self.small_enemies_layer.draw(self.screen)
            spawnSmallEnemy(elapsed_time, self.small_enemies_layer, self.player, self.hp_bar)

            self.explosion_layer.draw(self.screen)
            self.explosion_layer.update(3)

            self.gui_layer.draw(self.screen)

            self.hp_layer.draw(self.screen)
            self.hp_layer.update()

            self.timer.update(elapsed_time, self.screen)

            self.score.update(self.screen)

            self.checkCollision()

    def checkCollision(self):
        is_big_enemy_collide_with_player = pygame.sprite.groupcollide(self.big_enemies_layer, self.player_layer, True, False)
        if is_big_enemy_collide_with_player:
            self.createExplosion(is_big_enemy_collide_with_player)
            self.hp_bar.hp_diff += -3
            self.score.points += 2
        is_big_enemy_collide_with_beam = pygame.sprite.groupcollide(self.big_enemies_layer, self.beam_layer, True, True)
        if is_big_enemy_collide_with_beam:
            self.createExplosion(is_big_enemy_collide_with_beam)
            self.score.points += 5
        is_small_enemy_collide_with_player = pygame.sprite.groupcollide(self.small_enemies_layer, self.player_layer, True, False)
        if is_small_enemy_collide_with_player:
            self.createExplosion(is_small_enemy_collide_with_player)
            self.hp_bar.hp_diff += -2
            self.score.points += 1
        is_small_enemy_collide_with_beam = pygame.sprite.groupcollide(self.small_enemies_layer, self.beam_layer, True, True)
        if is_small_enemy_collide_with_beam:
            self.createExplosion(is_small_enemy_collide_with_beam)
            self.score.points += 2

    def createExplosion(self, collision_type):
        rect = list(collision_type.keys())[0].rect
        explosion = Explosion(rect.x + rect.width / 2, rect.y + rect.height / 2, rect.width)
        self.explosion_layer.add(explosion)
        explosion.animate()

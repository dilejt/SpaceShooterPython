from Sprite import Sprite


class Beam(Sprite):
    def __init__(self, player):
        self.beam_width = 6
        self.beam_height = 50
        super().__init__(player.x + player.player_width / 2 - self.beam_width / 2, player.y - self.beam_height, 'beam.png',
                         self.beam_width,
                         self.beam_height, 'beam.mp3')
        self.speed = 12
        self.sound.play()

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -self.beam_height:
            self.kill()

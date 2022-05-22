from Sprite import Sprite
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, GUI_HEIGHT


class Gui(Sprite):
    def __init__(self):
        super().__init__(-10, SCREEN_HEIGHT - GUI_HEIGHT, 'gui.jpg', SCREEN_WIDTH + 20, GUI_HEIGHT * 4)

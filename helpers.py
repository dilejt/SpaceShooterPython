import re

import pygame
from os import listdir, path


def getStrips(directory=''):
    directory = 'assets/pictures/' + directory
    return [pygame.image.load(directory + '/' + file) for file in
            sorted(filter(lambda x: path.isfile(path.join(directory, x)), listdir(directory)), key=lambda y: int(re.findall(r'\d+', y)[0]))]

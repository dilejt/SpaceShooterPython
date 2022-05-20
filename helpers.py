import pygame
from os import listdir
from os.path import isfile, join


def getStrips(directory=''):
    directory = 'assets/pictures/' + directory
    return [pygame.image.load(directory + '/' + file) for file in [f for f in listdir(directory) if isfile(
        join(directory, f))]]

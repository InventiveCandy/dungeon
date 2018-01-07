import pygame
from pygame.locals import *

from src import constants


"""
main.py

This is where the magic happens
"""


class Main:

    def __init__(self):

        pygame.init()

        self.display = pygame.display.set_mode(constants.DISPLAY_SIZE)
        pygame.display.set_caption("Dungeon")

    def run(self):

        pass


if __name__ == "__main__":

    game = Main()
    game.run()

    pygame.quit()

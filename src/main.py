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

        self.clock = pygame.time.Clock()

    def run(self):

        game_exit = False

        while not game_exit:

            for event in pygame.event.get():

                if event.type == QUIT:
                    game_exit = True

            self.display.fill(constants.WHITE)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":

    game = Main()
    game.run()

    pygame.quit()

#intro # I couldn't think of any better name to give to this file, so it is the "world" #

import pygame

from colors import *
from display import screen

class World:
    def __init__(self):
        self.width, self.height = 470, 333
        self.rect_to_fall = pygame.Rect(0, 0, self.width - 50, self.height)

        self._image = pygame.image.load("assets/gfx/world.png").convert()

    def draw(self) -> None: screen.blit(self._image, (0, 0))

world_instance = World()
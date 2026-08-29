#intro # I couldn't think of any better name to give to this file, so it is the "world" #

import pygame

from colors import *
from display import screen

class World:
    def __init__(self):
        self.width, self.height = 470, 333
        self.rect_to_fall = pygame.Rect(0, 0, self.width - 50, self.height)

        self._image = pygame.image.load("assets/gfx/world.png").convert()
        self._image_desk = pygame.image.load("assets/gfx/desk.png").convert_alpha()

        self._phone = pygame.image.load("assets/gfx/phone.png").convert_alpha()

    def draw(self) -> None:
        screen.blit(self._image, (0, 0))
        screen.blit(self._image_desk, (0, 0))

        screen.blit(self._phone, (self.width - self._phone.get_width() - 10, self.height - self._phone.get_height() - 5))

world_instance = World()
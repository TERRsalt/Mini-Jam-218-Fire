#intro # I couldn't think of any better name to give to this file, so it is the "world" #

import pygame

from colors import *
from display import screen
from shadow import Shadow

class World:
    def __init__(self):
        self.width, self.height = 470, 333
        self.rect_to_fall = pygame.Rect(0, 0, self.width - 50, self.height)

        self._image = pygame.image.load("assets/gfx/world.png").convert()

        self._image_sylwester = pygame.image.load("assets/gfx/sylwester.png").convert_alpha()
        self._shadow_sylwester = Shadow(self._image_sylwester)

        self._image_desk = pygame.image.load("assets/gfx/desk.png").convert_alpha()
        self._shadow_desk = Shadow(self._image_desk)
        self._phone = pygame.image.load("assets/gfx/phone.png").convert_alpha()

    def draw(self) -> None:
        screen.blit(self._image, (0, 0))

        screen.blit(self._shadow_sylwester.surface, (-self._shadow_sylwester.radius, -self._shadow_sylwester.radius))
        screen.blit(self._image_sylwester, (0, 0))

        screen.blit(self._shadow_desk.surface, (-self._shadow_desk.radius, -self._shadow_desk.radius))
        screen.blit(self._image_desk, (0, 0))
        screen.blit(self._phone, (self.width - self._phone.get_width() - 10, self.height - self._phone.get_height() - 5))

world_instance = World()
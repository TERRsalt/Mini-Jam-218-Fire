#intro # I couldn't think of any better name to give to this file, so it is the "world" #

import pygame
from enum import Enum

from colors import *
from display import screen, screen_width
from settings import screen_height
from shadow import Shadow

class SylwesterLook(Enum):
    SYLWESTER = 0
    DEVIL = 1

class World:
    def __init__(self):
        self.width, self.height = 470, 333

        self._image = pygame.image.load("assets/gfx/world.png").convert()

        self._image_sylwester = pygame.image.load("assets/gfx/sylwester.png").convert_alpha()
        self._shadow_sylwester = Shadow(self._image_sylwester)

        self._image_devil = pygame.image.load("assets/gfx/devil.png").convert_alpha()
        self._shadow_devil = Shadow(self._image_devil)

        self._image_desk = pygame.image.load("assets/gfx/desk.png").convert_alpha()
        self._shadow_desk = Shadow(self._image_desk)
        self._phone = pygame.image.load("assets/gfx/phone.png").convert_alpha()

        self.rect_to_fall = pygame.Rect(0, 0, self.width - 50, self.height)
        self.rect_on_the_right_to_fall = pygame.Rect(screen_width - 375, 0, 375, 600) #minor # I hope nobody sees this, because this code is one big mess @_@ #

    def draw(self, sylwester = None) -> None:
        screen.blit(self._image, (0, 0))

        if sylwester == SylwesterLook.SYLWESTER:
            screen.blit(self._shadow_sylwester.surface, (-self._shadow_sylwester.radius, -self._shadow_sylwester.radius))
            screen.blit(self._image_sylwester, (0, 0))
        elif sylwester == SylwesterLook.DEVIL:
            screen.blit(self._shadow_devil.surface, (-self._shadow_devil.radius, -self._shadow_devil.radius))
            screen.blit(self._image_devil, (0, 0))

        screen.blit(self._shadow_desk.surface, (-self._shadow_desk.radius, -self._shadow_desk.radius))
        screen.blit(self._image_desk, (0, 0))
        screen.blit(self._phone, (self.width - self._phone.get_width() - 10, self.height - self._phone.get_height() - 5))

        #pygame.draw.rect(screen, PURPLE, self.rect_on_the_right_to_fall)

world_instance = World()
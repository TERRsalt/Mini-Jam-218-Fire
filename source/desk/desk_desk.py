import pygame

from display import screen, screen_width, screen_height
from colors import *
from shadow import Shadow

from desk.mini_desk import mini_desk_instance
from desk.furnace_desk import furnace

class Desk:
    def __init__(self):
        self.xy = pygame.Vector2(mini_desk_instance.width + 3, 0)
        self.width, self.height = screen_width - (mini_desk_instance.width + furnace.width + 5), screen_height
        self._rect = pygame.Rect(self.xy.x, self.xy.y, self.width, self.height)

        self._border_surface = pygame.Surface((3, screen_height)).convert()
        self._border_surface.fill(YELLOW)
        self._shadow_border = Shadow(self._border_surface)

    def draw(self):
        pygame.draw.rect(screen, RED, self._rect)

        screen.blit(self._shadow_border.surface, (self.xy.x - 3 - self._shadow_border.radius, self.xy.y - self._shadow_border.radius))
        screen.blit(self._border_surface, (self.xy.x - 3, self.xy.y))

desk_instance = Desk() #minor # What a name #
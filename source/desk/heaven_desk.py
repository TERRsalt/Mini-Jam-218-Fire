import pygame

from colors import *
from display import screen, screen_width, screen_height
from shadow import Shadow

from desk.furnace_desk import furnace

class Heaven:
    def __init__(self):
        self.width, self.height = furnace.width, screen_height - furnace.height
        self.xy = pygame.Vector2(screen_width - self.width, screen_height - self.height)
        self._rect = pygame.Rect(self.xy.x, self.xy.y, self.width, self.height)

        self._border_bottom_right = pygame.Surface((self.width, 3)).convert()
        self._border_bottom_right.fill(WHITE)
        self._shadow_border_top_left = Shadow(self._border_bottom_right)

    def draw(self):
        pygame.draw.rect(screen, YELLOW, self._rect)

        screen.blit(self._shadow_border_top_left.surface, (self.xy.x - self._shadow_border_top_left.radius, self.xy.y - self._shadow_border_top_left.radius))
        screen.blit(self._border_bottom_right, self.xy)

heaven = Heaven()
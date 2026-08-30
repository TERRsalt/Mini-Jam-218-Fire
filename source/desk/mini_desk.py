import pygame

from colors import *
from display import screen
from settings import screen_height
from shadow import Shadow

from desk.world import world_instance

class MiniDesk:
    def __init__(self):
        self.width, self.height = world_instance.width, screen_height - world_instance.height
        self.y = screen_height - self.height
        self._rect = pygame.Rect(0, self.y, self.width, self.height)

        self._border_top_left_surface = pygame.Surface((self.width, 3)).convert()
        self._border_top_left_surface.fill(YELLOW)
        self._shadow_border_top_left = Shadow(self._border_top_left_surface)

    def draw(self):
        pygame.draw.rect(screen, RED, self._rect)

        screen.blit(self._shadow_border_top_left.surface, (-self._shadow_border_top_left.radius, self.y - self._shadow_border_top_left.radius))
        screen.blit(self._border_top_left_surface, (0, self.y))

mini_desk_instance = MiniDesk()
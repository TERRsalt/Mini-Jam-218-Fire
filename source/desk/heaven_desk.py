import pygame

from colors import *
from display import screen, screen_width, screen_height
from fonts import font
from shadow import Shadow

from desk.furnace_desk import furnace
from text_funs import render_text_in_the_middle

class Heaven:
    def __init__(self):
        self.width, self.height = furnace.width, screen_height - furnace.height
        self.xy = pygame.Vector2(screen_width - self.width, screen_height - self.height)
        self.rect = pygame.Rect(self.xy.x, self.xy.y, self.width, self.height)

        self._border_bottom_right = pygame.Surface((self.width, 3)).convert()
        self._border_bottom_right.fill(WHITE)
        self._shadow_border_top_left = Shadow(self._border_bottom_right)

        self._text = font.retron_2000_size_54.render("H.E.A.V.E.N.", False, WHITE)

    def draw(self):
        pygame.draw.rect(screen, YELLOW, self.rect)

        render_text_in_the_middle(self._text, screen, pygame.Vector2(self.xy.x, screen_height - 224), self.width)

        screen.blit(self._shadow_border_top_left.surface, (self.xy.x - self._shadow_border_top_left.radius, self.xy.y - self._shadow_border_top_left.radius))
        screen.blit(self._border_bottom_right, self.xy)

heaven = Heaven()
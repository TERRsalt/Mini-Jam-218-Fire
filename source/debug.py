import pygame

from colors import *
from display import screen
from fonts import font

class Debug:
    def __init__(self):
        self.should_draw = False

        self._previous_text = None
        self._text_surface = None
        self._width, self._height = 0, 0

    def _controls(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F3: self.should_draw = not self.should_draw

    def draw(self, events, text, xy = pygame.Vector2(0, 0)) -> None:
        self._controls(events)

        if not self.should_draw: return

        if self._previous_text != text:
            self._previous_text = text

            self._text_surface = font.retron_2000_size_27.render(text, False, WHITE)
            self._width, self._height = self._text_surface.get_width() + 10, self._text_surface.get_height() + 10

        pygame.draw.rect(screen, BLACK, pygame.Rect(xy.x, xy.y, self._width, self._height))
        screen.blit(self._text_surface, (xy.x + 5, xy.y + 5))

debug_menu = Debug()
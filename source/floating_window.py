import pygame

from colors import *
from clickable import clickables
from display import screen_width, screen_height

class Dragging:
    def __init__(self): self.currently_dragging = None

    def is_player_dragging_a_window(self, floating_window) -> bool:
        if self.currently_dragging is None:
            self.currently_dragging = floating_window
            return True
        return False

dragging = Dragging()

class FloatingWindow:
    def __init__(self, xy, width, height, should_draw = True):
        self._width, self._height = width, height
        self.xy = pygame.Vector2(xy) if xy is not None else pygame.Vector2((screen_width - self._width) // 2, (screen_height - self._height) // 2)
        self._surface = pygame.Surface((self._width, self._height)).convert_alpha()
        self._surface.fill(TRANSPARENT)
        self._background = pygame.Rect(self.xy.x, self.xy.y, self._width, self._height)

        self.should_draw = should_draw

        self._offset = pygame.Vector2()

    def _controls(self, events, mouse) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self._background.collidepoint(mouse) and dragging.is_player_dragging_a_window(self):
                self._offset = self.xy - mouse
                self._background.x = int(self.xy.x)
                self._background.y = int(self.xy.y)

            elif event.type == pygame.MOUSEBUTTONUP: dragging.currently_dragging = None

            if event.type == pygame.MOUSEMOTION and dragging.currently_dragging == self:
                self.xy = mouse + self._offset
                self.xy.x = max(0, min(screen_width - self._width, self.xy.x))
                self.xy.y = max(0, min(screen_height - self._height, self.xy.y))
                self._background.x = int(self.xy.x)
                self._background.y = int(self.xy.y)

        if self._background.collidepoint(mouse): clickables.add(1000)
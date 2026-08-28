import pygame

from colors import *
from clickable import clickables
from display import screen_width, screen_height

class FloatingWindow: #info # Create subclasses #
    def __init__(self, xy, width, height, should_draw = True):
        self._width, self._height = width, height
        self._xy = pygame.Vector2(xy) if xy is not None else pygame.Vector2((screen_width - self._width) // 2, (screen_height - self._height) // 2)
        self._surface = pygame.Surface((self._width, self._height)).convert_alpha()
        self._surface.fill(TRANSPARENT)
        self._background = pygame.Rect(self._xy.x, self._xy.y, self._width, self._height)

        self.should_draw = should_draw

        self._dragging = False
        self._offset = pygame.Vector2()

    def _controls(self, events, mouse) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self._background.collidepoint(mouse):
                self._dragging = True
                self._offset = self._xy - mouse
                self._background.x = int(self._xy.x)
                self._background.y = int(self._xy.y)

            elif event.type == pygame.MOUSEBUTTONUP: self._dragging = False

            if event.type == pygame.MOUSEMOTION and self._dragging:
                self._xy = mouse + self._offset
                self._xy.x = max(0, min(screen_width - self._width, self._xy.x))
                self._xy.y = max(0, min(screen_height - self._height, self._xy.y))
                self._background.x = int(self._xy.x)
                self._background.y = int(self._xy.y)

        if self._background.collidepoint(mouse): clickables.add(1000)
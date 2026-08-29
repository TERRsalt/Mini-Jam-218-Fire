import pygame

from colors import *
from clickable import clickables
from display import screen_width, screen_height

#info # `Dragging` #

class Dragging:
    def __init__(self): self.currently_dragging = None

    def is_player_dragging_a_window(self, floating_window) -> bool:
        if self.currently_dragging is None:
            self.currently_dragging = floating_window
            return True
        return False

dragging = Dragging()

#info # `FloatingWindow` #

floating_windows = []

class FloatingWindow:
    def __init__(self, xy, width, height, should_draw = True):
        self.width, self.height = width, height
        self.xy = pygame.Vector2(xy) if xy is not None else pygame.Vector2((screen_width - self.width) // 2, (screen_height - self.height) // 2)
        self._surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self._surface.fill(TRANSPARENT)
        self.background = pygame.Rect(self.xy.x, self.xy.y, self.width, self.height)

        self.should_draw = should_draw

        self._offset = pygame.Vector2()

    def _controls(self, events, mouse) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.background.collidepoint(mouse):
                colliding = [floating_window for floating_window in floating_windows if floating_window.background.collidepoint(mouse)]
                if colliding and colliding[0] == self and dragging.is_player_dragging_a_window(self):
                    floating_windows.insert(0, floating_windows.pop(floating_windows.index(self)))
                    self._offset = self.xy - mouse
                    self.background.x = int(self.xy.x)
                    self.background.y = int(self.xy.y)

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging.currently_dragging = None

            if event.type == pygame.MOUSEMOTION and dragging.currently_dragging == self:
                self.xy = mouse + self._offset
                self.xy.x = max(0, min(screen_width - self.width, self.xy.x))
                self.xy.y = max(0, min(screen_height - self.height, self.xy.y))
                self.background.x = int(self.xy.x)
                self.background.y = int(self.xy.y)

        if self.background.collidepoint(mouse):
            clickables.add(1000)
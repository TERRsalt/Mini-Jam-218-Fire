import pygame

from colors import *
from display import screen, screen_height
from interval_time import interval
from fonts import font

from desk.document import documents

class Furnace:
    def __init__(self):
        self.temperature = 666

        self._xy = pygame.Vector2(1501, 0)
        self._width, self._height = 419, screen_height

        self._surface = pygame.Surface((self._width, self._height))
        self._surface.fill(RED)

        self._rect = pygame.Rect(self._xy.x, self._xy.y, self._width, self._height)

    def _logic(self, events, mouse):
        if interval(500): self.temperature -= 1

        for i in range(len(documents)):
            if documents[i].look.xy.x > self._xy.x:
                documents[i].look.should_draw = False
                documents[i].look.xy.x = 0
                self.temperature += documents[i].sum_of_sins_and_virtues

    def draw(self, events, mouse):
        self._logic(events, mouse)

        screen.blit(self._surface, self._xy)

        screen.blit(font.retron_2000_size_27.render(f"{self.temperature}", False, WHITE), (1800, 100))

furnace = Furnace()
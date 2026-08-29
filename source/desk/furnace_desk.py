import pygame

from colors import *
from display import screen, screen_width, screen_height
from interval_time import interval
from fonts import font
from shadow import Shadow

from desk.document import documents

class Furnace:
    def __init__(self):
        self.temperature = 666
        self.last_temperature = 666
        self.planned_temperature = 0
        self.temperature_change = 0

        self.width, self.height = 451, screen_height - 333
        self.xy = pygame.Vector2(screen_width - self.width, 0)

        self._surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self._surface.fill(YELLOW)

        self._border_surface = pygame.Surface((3, screen_height)).convert()
        self._border_surface.fill(WHITE)
        self._shadow_border = Shadow(self._border_surface)

        self._rect = pygame.Rect(self.xy.x, self.xy.y, self.width, self.height)

    def _logic(self, events, mouse):
        if interval(500):
            if self.temperature_change == 0:
                if self.planned_temperature > 0: self.temperature_change = 1
                elif self.planned_temperature < 0: self.temperature_change = -1

            if self.planned_temperature != 0: self.planned_temperature -= self.temperature_change
            else: self.temperature_change = 0

            self.temperature += self.temperature_change - 1

        for i in range(len(documents)):
            if documents[i].look.xy.x > self.xy.x:
                documents[i].look.should_draw = False
                documents[i].look.xy.x = 0
                self.planned_temperature += documents[i].sum_of_sins_and_virtues

                if documents[i].sum_of_sins_and_virtues > 0: self.temperature_change += 1
                else: self.temperature_change -= 1

    def draw(self, events, mouse):
        self._logic(events, mouse)

        screen.blit(self._surface, self.xy)

        screen.blit(font.retron_2000_size_27.render(f"Temperature: {self.temperature}", False, WHITE), (1600, 100))
        screen.blit(font.retron_2000_size_27.render(f"Planned: {self.planned_temperature}", False, WHITE), (1600, 200))
        screen.blit(font.retron_2000_size_27.render(f"Change: {self.temperature_change}", False, WHITE), (1600, 300))

        screen.blit(self._shadow_border.surface, (self.xy.x - 2 - self._shadow_border.radius, self.xy.y - self._shadow_border.radius))
        screen.blit(self._border_surface, (self.xy.x - 2, self.xy.y))

furnace = Furnace()
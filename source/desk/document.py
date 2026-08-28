from zoneinfo import available_timezones

import pygame
import random

from colors import WHITE
from display import screen
from floating_window import FloatingWindow
from shadow import Shadow
from fonts import font
from colors import *

_DICTIONARY_OF_ALL_SINS = {
    "Murder": 66,
    "Thief": 40,
    "Lying": 30,
}

class Document:
    def __init__(self):
        max_sins_value = random.randint(10, 100)
        self.sins = {}
        available_sins = _DICTIONARY_OF_ALL_SINS.copy()
        while max_sins_value > sum(self.sins.values()):
            random_sin = random.choice(list(available_sins.items()))
            available_sins.pop(random_sin[0])
            self.sins[random_sin[0]] = random_sin[1]
        self.sum_of_sins_and_virtues = sum(self.sins.values())

        class DocumentDraw(FloatingWindow):
            def __init__(self, parent, xy, width, height):
                super().__init__(xy, width, height)
                self._parent = parent

                self._surface.fill(WHITE)
                y = 0
                for sin, temperature in self._parent.sins.items():
                    if temperature >= 0: self._surface.blit(font.departure_mono_size_22.render(f"{sin} (+{temperature}°C)", False, RED), (0, y))
                    else: self._surface.blit(font.departure_mono_size_22.render(f"{sin} ({temperature}°C)", False, RED), (0, y))
                    y += 22

                self._shadow = Shadow(self._surface)

            def draw(self, events, mouse) -> None:
                if not self.should_draw: return

                self._controls(events, mouse)

                screen.blit(self._shadow.surface, (self.xy.x - self._shadow.radius, self.xy.y - self._shadow.radius))
                screen.blit(self._surface, self.xy)

        self.look = DocumentDraw(self, None, 300, 300)

    def draw(self, events, mouse) -> None: self.look.draw(events, mouse)

documents = [
    Document(),
    Document(),
    Document()
]
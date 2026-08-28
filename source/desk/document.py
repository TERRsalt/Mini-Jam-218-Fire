import pygame
import random

from colors import WHITE
from display import screen
from floating_window import FloatingWindow
from shadow import Shadow
from fonts import font
from colors import *

#todo # Look up this sins and virtues made by AI and improve on them #

_DICTIONARY_OF_ALL_SINS = {
    "Murder": 100,
    "Treason": 90,
    "Cruelty": 80,
    "Extortion": 70,

    "Arson": 60,
    "Grand Theft": 50,
    "Embezzlement": 40,
    "Adultery": 35,
    "Corruption": 30,

    "Fraud": 25,
    "Perjury": 20,
    "Vandalism": 15,
    "Greed": 15,
    "Gluttony": 10,
    "Envy": 10,
    "Sloth": 10,
    "Lying": 5,
    "Gossiping": 5,
    "Tardiness": 5,
    "Swearing": 5
}

_DICTIONARY_OF_ALL_VIRTUES = {
    "Self-sacrifice": -100,
    "Saved a Life": -90,
    "Lifelong Charity": -80,
    "Forgave Enemy": -70,

    "Adopted a Stray": -60,
    "Donated Wealth": -50,
    "Volunteer Work": -40,
    "Return Lost Wallet": -30,

    "Helped Neighbor": -25,
    "Gave Up Seat": -20,
    "Fed Homeless": -15,
    "Kind Words": -10,
    "Politeness": -5,
    "Honesty": -5
}

class Document:
    def __init__(self):
        while True:
            max_sins_value = random.randint(10, 200) #todo # Add minus values for better chances #
            self.sins = {}
            available_sins = _DICTIONARY_OF_ALL_SINS.copy()
            while max_sins_value > sum(self.sins.values()):
                random_sin = random.choice(list(available_sins.items()))
                available_sins.pop(random_sin[0])
                self.sins[random_sin[0]] = random_sin[1]

            max_virtues_value = -random.randint(10, 150)
            self.virtues = {}
            available_virtues = _DICTIONARY_OF_ALL_VIRTUES.copy()
            while max_virtues_value < sum(self.virtues.values()):
                random_virtue = random.choice(list(available_virtues.items()))
                available_virtues.pop(random_virtue[0])
                self.virtues[random_virtue[0]] = random_virtue[1]

            self.sum_of_sins_and_virtues = sum(self.sins.values()) + sum(self.virtues.values())
            if self.sum_of_sins_and_virtues != 0: break

        class DocumentDraw(FloatingWindow):
            def __init__(self, parent, xy, width, height):
                super().__init__(xy, width, height)
                self._parent = parent

                self._surface.fill(WHITE)
                y = 0
                for sin, temperature in self._parent.sins.items():
                    self._surface.blit(font.departure_mono_size_22.render(f"{sin} (+{temperature}°C)", False, RED), (0, y))
                    y += 22

                y += 22
                for virtue, temperature in self._parent.virtues.items():
                    self._surface.blit(font.departure_mono_size_22.render(f"{virtue} ({temperature}°C)", False, RED), (0, y))
                    y += 22

                y += 22
                self._surface.blit(font.departure_mono_size_22.render(f"DEBUG: ({self._parent.sum_of_sins_and_virtues}°C)", False, RED), (0, y))

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
import pygame
import random

from colors import *
from display import screen
from floating_window import FloatingWindow, floating_windows
from settings import screen_width, screen_height
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
        self.name = "Ron Random"

        #info # Sins and virtues #

        while True:
            max_virtues_value = -random.randint(-10, 100)
            max_sins_value = random.randint(-10, 200 + max_virtues_value // 2)

            self.sins = {}
            available_sins = _DICTIONARY_OF_ALL_SINS.copy()
            try: sum_of_sins = sum(self.sins.values())
            except ValueError: sum_of_sins = 0
            while max_sins_value > sum_of_sins:
                sum_of_sins = sum(self.sins.values())
                random_sin = random.choice(list(available_sins.items()))
                available_sins.pop(random_sin[0])
                self.sins[random_sin[0]] = random_sin[1]

            self.virtues = {}
            available_virtues = _DICTIONARY_OF_ALL_VIRTUES.copy()
            try: sum_of_virtues = sum(self.virtues.values())
            except ValueError: sum_of_virtues = 0
            while max_virtues_value < sum_of_virtues:
                sum_of_virtues = sum(self.virtues.values())
                random_virtue = random.choice(list(available_virtues.items()))
                available_virtues.pop(random_virtue[0])
                self.virtues[random_virtue[0]] = random_virtue[1]

            try: sum_of_sins = sum(self.sins.values())
            except ValueError: sum_of_sins = 0
            try: sum_of_virtues = sum(self.virtues.values())
            except ValueError: sum_of_virtues = 0

            self.sum_of_sins_and_virtues = sum_of_sins + sum_of_virtues
            if self.sum_of_sins_and_virtues != 0: break

        additional_height = 0
        if sum_of_sins != 0: additional_height += 44 + len(self.sins) * 22
        if sum_of_virtues != 0: additional_height += 44 + len(self.virtues) * 22

        class DocumentDraw(FloatingWindow):
            def __init__(self, parent, xy, width, height):
                super().__init__(xy, width, height)
                self._parent = parent

                self._surface.fill(WHITE)
                pygame.draw.rect(self._surface, YELLOW, pygame.Rect(0, 0, self.width, self.height), 1)
                text_xy = pygame.Vector2(4, 0)

                self._surface.blit(font.departure_mono_size_22.render(self._parent.name, False, RED), text_xy)
                self._surface.blit(font.departure_mono_size_22.render(f"{self._parent.sum_of_sins_and_virtues}", False, RED), (200, text_xy.y))
                text_xy.y += 22

                if len(self._parent.sins) != 0:
                    text_xy.y += 22
                    self._surface.blit(font.departure_mono_size_22.render("Sins:", False, RED), text_xy)
                    text_xy.y += 22
                    for sin, temperature in self._parent.sins.items():
                        self._surface.blit(font.departure_mono_size_22.render(f" - {sin} (+{temperature}°C)", False, RED), text_xy)
                        text_xy.y += 22

                if len(self._parent.virtues) != 0:
                    text_xy.y += 22
                    self._surface.blit(font.departure_mono_size_22.render("Virtues:", False, RED), text_xy)
                    text_xy.y += 22
                    for virtue, temperature in self._parent.virtues.items():
                        self._surface.blit(font.departure_mono_size_22.render(f" - {virtue} ({temperature}°C)", False, RED), text_xy)
                        text_xy.y += 22
                text_xy.y -= 22

                text_xy.y += 44
                self._surface.blit(font.departure_mono_size_22.render(f"DEBUG: {self._parent.sum_of_sins_and_virtues}°C", False, RED), text_xy)

                self._shadow = Shadow(self._surface)

            def draw(self, events, mouse) -> None:
                if not self.should_draw: return

                self._controls(events, mouse)

                screen.blit(self._shadow.surface, (self.xy.x - self._shadow.radius, self.xy.y - self._shadow.radius))
                screen.blit(self._surface, self.xy)

        self.look = DocumentDraw(self, pygame.Vector2((screen_width - 451 - 1000) + 5, 5), 450, 28 + additional_height)

    def draw(self, events, mouse) -> None: self.look.draw(events, mouse)

documents = []
for i in range(25): documents.append(Document())
_max_height_of_documents = max(document.look.height for document in documents)
documents.sort(key = lambda document: document.look.height, reverse = False)
for document in documents:
    random_additional_xy = pygame.Vector2(random.randint(1, 6), random.randint(1, 6))

    document.look.xy.x += random_additional_xy.x
    document.look.background.x += random_additional_xy.x

    additional_y = _max_height_of_documents - document.look.height + random_additional_xy.y
    document.look.xy.y += additional_y
    document.look.background.y += additional_y

    floating_windows.append(document.look)
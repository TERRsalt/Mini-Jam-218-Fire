import pygame
import random

from colors import *
from desk.mini_desk import mini_desk_instance
from desk.names import *
from desk.timer import timer_instance
from desk.world import world_instance
from display import screen
from floating_window import FloatingWindow, floating_windows, dragging
from settings import screen_width, screen_height
from shadow import Shadow
from fonts import font
from colors import *
from desk.days import *

#info # These (2 dictionaries) were made up by the AI #

DICTIONARY_OF_ALL_SINS = {
    # Tiny, everyday sins (common)
    "Interrupting":       2,
    "Swearing":           4,
    "Littering":          5,
    "Oversleeping":       6,
    "Talking Loudly":     6,
    "Cutting in Line":    7,
    "Fibbing":            8,
    "Procrastination":    9,
    "Complaining":        9,
    "Gossiping":         10,
    "Vanity":            11,
    "Overeating":        12,
    "Skipping Chores":   12,
    "Rudeness":          13,
    "Ghosting Someone":  14,
    "Spreading Rumors":  15,
    "Laziness":          16,
    "Jealousy":          17,
    "Petty Insults":     18,
    "Mockery":           19,
    "Overdrinking":      20,

    # Low-moderate sins
    "Minor Cheating":    22,
    "Overindulgence":    24,
    "Blasphemy":         26,
    "Envy":              28,
    "Pride":             30,
    "Public Tantrum":    31,
    "Breaking a Promise":33,
    "Cyberbullying":     35,
    "Lying":             38,
    "Gluttony":          40,

    # Moderate sins (less common)
    "Greed":             45,
    "Manipulation":      50,
    "Infidelity":        55,
    "Bullying":          58,
    "Theft":             62,
    "Fraud":             66,
    "Corruption":        70,
    "Lust":              73,

    # Severe sins (rare)
    "Betrayal":          78,
    "Wrath":             82,
    "Assault":           86,
    "Slavery":           90,
    "Torture":           94,

    # Extreme sins (extremely rare — near the cap)
    "Murder":            97,
    "Genocide":         100,
}

DICTIONARY_OF_ALL_VIRTUES = {
    # Tiny, everyday virtues (common)
    "Saying Thank You":   -2,
    "Holding the Door":   -3,
    "Smiling at Someone": -4,
    "Recycling":          -5,
    "Being On Time":      -6,
    "Listening Well":     -6,
    "Waiting Your Turn":  -7,
    "Small Compliment":   -8,
    "Tidying Up":         -9,
    "Gratitude":          -9,
    "Cheerfulness":      -10,
    "Modesty":           -11,
    "Sharing Food":      -12,
    "Doing Chores":      -12,
    "Politeness":        -13,
    "Checking In on Someone": -14,
    "Encouraging a Friend": -15,
    "Diligence":         -16,
    "Patience":          -17,
    "Helping a Stranger":-18,
    "Sincere Apology":   -19,
    "Volunteering":      -20,

    # Low-moderate virtues
    "Minor Honesty":     -22,
    "Temperance":        -24,
    "Fairness":          -26,
    "Loyalty":           -28,
    "Kindness":          -30,
    "Standing Up for Someone": -31,
    "Keeping a Promise": -33,
    "Comforting Someone":-35,
    "Humility":          -38,
    "Honesty":           -40,

    # Moderate virtues (less common)
    "Generosity":        -45,
    "Chastity":          -50,
    "Forgiveness":       -55,
    "Charity":           -58,
    "Courage":           -62,
    "Justice":           -66,
    "Compassion":        -70,
    "Wisdom":            -73,

    # Profound virtues (rare)
    "Mercy":             -78,
    "Devotion":          -82,
    "Selflessness":      -86,
    "Sacrifice":         -90,
    "Heroic Rescue":     -94,

    # Transcendent virtues (extremely rare — near the cap)
    "Redemption":         -97,
    "Unconditional Love": -100,
}

_DOCUMENT_TOP = pygame.image.load("assets/gfx/document_top.png").convert_alpha()

class Document:
    def __init__(self):
        self.name = names[random.randint(0, names_length - 1)]

        #info # Sins and virtues #

        while True:
            max_virtues_value = -random.randint(-10, 150)
            max_sins_value = random.randint(-10, 200)

            self.sins = {}
            available_sins = DICTIONARY_OF_ALL_SINS.copy()
            try: sum_of_sins = sum(self.sins.values())
            except ValueError: sum_of_sins = 0
            while max_sins_value > sum_of_sins:
                sum_of_sins = sum(self.sins.values())
                random_sin = random.choice(list(available_sins.items()))
                available_sins.pop(random_sin[0])
                self.sins[random_sin[0]] = random_sin[1]

            self.virtues = {}
            available_virtues = DICTIONARY_OF_ALL_VIRTUES.copy()
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

            self.sum_of_sins = sum_of_sins
            self.sum_of_sins_and_virtues = sum_of_sins + sum_of_virtues
            if self.sum_of_sins_and_virtues != 0: break

        additional_height = 0
        if sum_of_sins != 0: additional_height += 44 + len(self.sins) * 22
        if sum_of_virtues != 0: additional_height += 44 + len(self.virtues) * 22

        class DocumentDraw(FloatingWindow):
            def __init__(self, parent, xy, width, height):
                super().__init__(xy, width, height)
                self._parent = parent

                pygame.draw.rect(self._surface, WHITE, pygame.Rect(0, 25, self.width, self.height - 25))
                pygame.draw.rect(self._surface, YELLOW, pygame.Rect(0, 25, self.width, self.height - 25), 1)
                pygame.draw.rect(self._surface, WHITE, pygame.Rect(1, 25, self.width - 2, 1))
                self._surface.blit(_DOCUMENT_TOP, (0, 0))

                text_xy = pygame.Vector2(4, 25)

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

                self._shadow = Shadow(self._surface, 2)

            def draw(self, events, mouse) -> None:
                if not self.should_draw: return

                self._controls(events, mouse)

                if (self.rect.colliderect(world_instance.rect_to_fall) or self.rect.colliderect(world_instance.rect_on_the_right_to_fall)) \
                        and not dragging.currently_dragging:
                    self.xy.y += 20
                    self.rect.y += 20

                screen.blit(self._shadow.surface, (self.xy.x - self._shadow.radius, self.xy.y - self._shadow.radius))
                screen.blit(self._surface, self.xy)

        height_of_look = 28 + additional_height + 25
        self.look = DocumentDraw(self, pygame.Vector2(7, screen_height - 7 - height_of_look), 450, height_of_look)

    def draw(self, events, mouse) -> None: self.look.draw(events, mouse)

documents  = []
def reset_day() -> None:
    global documents

    documents = []
    floating_windows.clear()
    for i in range(spawned_documents[global_dictionary["days"] - 1]): documents.append(Document())
    _max_height_of_documents = max(document.look.height for document in documents)
    documents.sort(key = lambda document: document.look.height, reverse = False)
    for document in documents:
        random_additional_xy = pygame.Vector2(random.randint(1, 6), random.randint(-6, 0))

        document.look.xy.x += random_additional_xy.x
        document.look.rect.x += random_additional_xy.x

        document.look.xy.y += random_additional_xy.y
        document.look.rect.y += random_additional_xy.y

        floating_windows.append(document.look)

    global_dictionary["mistakes"] = 0
    global_dictionary["burned_documents"] = 0
    timer_instance.times_up = False
    timer_instance.time_in_seconds = 5 * 60 + 3
    timer_instance.minutes = 5
    timer_instance.seconds = 3
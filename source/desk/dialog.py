import pygame

from enum import Enum

from colors import *
from display import screen
from fonts import font
from interval_time import interval
from shadow import Shadow
from text_funs import render_text_in_the_middle

class Voice(Enum):
    SYLWESTER = 0
    PHONE = 1
    SYLWESTER_ANGRY = 2

_SYLWESTER_SOUNDS = pygame.mixer.Sound("assets/sfx/sylwester.ogg")
_PHONE_SOUNDS = pygame.mixer.Sound("assets/sfx/phone.ogg")
_SYLWESTER_ANGRY_SOUNDS = pygame.mixer.Sound("assets/sfx/sylwester_angry.ogg")

class Dialog:
    def __init__(self, full_message, who_is_talking):
        self.should_draw = True

        self._dialog_window = pygame.image.load("assets/gfx/dialog.png").convert_alpha()
        if who_is_talking == Voice.SYLWESTER: self._dialog_window.blit(pygame.image.load("assets/gfx/dialog_sylwester.png").convert_alpha(), (0, 0))
        else: self._dialog_window.blit(pygame.image.load("assets/gfx/dialog_phone.png").convert_alpha(), (0, 0))

        self._shadow_dialog = Shadow(self._dialog_window)

        self._full_message = full_message
        self._message_number = 0
        self._number_of_letters = 0
        self._should_dialog_increase_number_of_letters = True

        self.sylwester_talking = True

    def _controls(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if len(self._full_message[self._message_number]) > self._number_of_letters: self._number_of_letters = len(self._full_message[self._message_number])
                else:
                    self._number_of_letters = 0
                    self._message_number += 1

                    if self._message_number == len(self._full_message): self.should_draw = False

    def draw(self, events, voice):
        if not self.should_draw:
            self.sylwester_talking = False
            return

        screen.blit(self._shadow_dialog.surface, (-self._shadow_dialog.radius, -self._shadow_dialog.radius))
        screen.blit(self._dialog_window, (0, 0))

        self._controls(events)
        if not self.should_draw: #minor # Yes, I'm checking it again, because I don't have time to code it properly ^-^ #
            self.sylwester_talking = False
            return

        if len(self._full_message[self._message_number]) != self._number_of_letters:
            if interval(66, "dialog") and self._should_dialog_increase_number_of_letters:
                self._number_of_letters += 1
                self._should_dialog_increase_number_of_letters = False
            elif not interval(66, "dialog"): self._should_dialog_increase_number_of_letters = True

            if voice == Voice.SYLWESTER and _SYLWESTER_SOUNDS.get_num_channels() == 0: _SYLWESTER_SOUNDS.play()

        rendered_message = font.departure_mono_size_22.render(self._full_message[self._message_number][:self._number_of_letters], False, WHITE)
        render_text_in_the_middle(rendered_message, screen, pygame.Vector2(2, 255), self._dialog_window.get_width() - 2)

message_1 = [
    "The brown fox jumps over the edge",
    "Second message",
    "Wow, a third message!"
]
dialog_1 = Dialog(message_1, Voice.PHONE)
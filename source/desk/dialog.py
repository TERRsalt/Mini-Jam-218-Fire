import pygame

from enum import Enum

from colors import *
from display import screen
from fonts import font
from interval_time import interval, previous_times
from shadow import Shadow
from text_funs import render_text_in_the_middle

class Voice(Enum):
    SYLWESTER = 0
    PHONE = 1
    DEVIL = 2

_SYLWESTER_SOUNDS = pygame.mixer.Sound("assets/sfx/sylwester.ogg")
_PHONE_SOUNDS = pygame.mixer.Sound("assets/sfx/phone.ogg")
_DEVIL_SOUNDS = pygame.mixer.Sound("assets/sfx/sylwester_angry.ogg")

class Dialog:
    def __init__(self, full_message, who_is_talking):
        self.should_draw = True

        self._dialog_window = pygame.image.load("assets/gfx/dialog.png").convert_alpha()
        self.who_is_talking = who_is_talking
        if who_is_talking == Voice.SYLWESTER or who_is_talking == Voice.DEVIL:
            self._dialog_window.blit(pygame.image.load("assets/gfx/dialog_sylwester.png").convert_alpha(), (0, 0))
        else: self._dialog_window.blit(pygame.image.load("assets/gfx/dialog_phone.png").convert_alpha(), (0, 0))

        self._shadow_dialog = Shadow(self._dialog_window)

        self._full_message = full_message
        self._message_number = 0
        self._number_of_letters = 0
        self._should_dialog_increase_number_of_letters = True

        self.sylwester_talking = True

    def reset(self):
        self._message_number = 0
        self._number_of_letters = 0
        self._should_dialog_increase_number_of_letters = True
        self.should_draw = True
        self.sylwester_talking = True
        previous_times["dialog"] = pygame.time.get_ticks()

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
        if not self.should_draw:
            self.sylwester_talking = False
            return

        if len(self._full_message[self._message_number]) != self._number_of_letters:
            should_advance = interval(66, "dialog")

            if should_advance and self._should_dialog_increase_number_of_letters:
                self._number_of_letters += 1
                self._should_dialog_increase_number_of_letters = False
            elif not should_advance:
                self._should_dialog_increase_number_of_letters = True

            if voice == Voice.SYLWESTER and _SYLWESTER_SOUNDS.get_num_channels() == 0: _SYLWESTER_SOUNDS.play()
            elif voice == Voice.PHONE and _PHONE_SOUNDS.get_num_channels() == 0: _PHONE_SOUNDS.play()
            elif voice == Voice.DEVIL and _DEVIL_SOUNDS.get_num_channels() == 0: _DEVIL_SOUNDS.play()

        else: previous_times["dialog"] = pygame.time.get_ticks()

        rendered_message = font.departure_mono_size_22.render(self._full_message[self._message_number][:self._number_of_letters], False, WHITE)
        render_text_in_the_middle(rendered_message, screen, pygame.Vector2(2, 255), self._dialog_window.get_width() - 2)
import pygame

import settings
from clickable import clickables

from colors import *
from floating_window import FloatingWindow
from fonts import font
from shadow import Shadow
from display import screen, resize_screen
from floating_window import floating_windows

class Settings(FloatingWindow):
    def __init__(self, xy, width, height):
        super().__init__(xy, width, height, False)
        self._surface.fill(WHITE)

        self._screen_width_value = settings.screen_width
        self._screen_height_value = settings.screen_height
        self._fullscreen_value = settings.fullscreen

        self._screen_width_text = font.departure_mono_size_22.render(f"Screen width: {self._screen_width_value}", False, RED)
        self._screen_height_text = font.departure_mono_size_22.render(f"Screen height: {self._screen_height_value}", False, RED)
        self._fullscreen_text = font.departure_mono_size_22.render(f"Fullscreen: {self._fullscreen_value}", False, RED)

        self._shadow = Shadow(self._surface)

        self._apply_button = self._plus_screen_width = self._plus_screen_height = self._minus_screen_width = self._minus_screen_height = \
                 self._toggle_fullscreen = self._set_screen_resolution_button = pygame.Rect(0, 0, 0, 0)

    def _controls_settings_main_menu(self, events, mouse):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                surface_mouse = mouse - self.xy

                if self._apply_button.collidepoint(surface_mouse): clickables.add(1001, lambda: self._apply_method(), "click")
                elif self._set_screen_resolution_button.collidepoint(surface_mouse): clickables.add(1001, lambda: self._set_screen_resolution(), "click")

                elif self._plus_screen_width.collidepoint(surface_mouse): clickables.add(1001, lambda: self._change_screen_width(self._screen_width_value + 10), "click")
                elif self._minus_screen_width.collidepoint(surface_mouse): clickables.add(1001, lambda: self._change_screen_width(self._screen_width_value - 10), "click")

                elif self._plus_screen_height.collidepoint(surface_mouse): clickables.add(1001, lambda: self._change_screen_height(self._screen_height_value + 10), "click")
                elif self._minus_screen_height.collidepoint(surface_mouse): clickables.add(1001, lambda: self._change_screen_height(self._screen_height_value - 10), "click")

                elif self._toggle_fullscreen.collidepoint(surface_mouse): clickables.add(1001, lambda: self._toggle_fullscreen_method(), "click")

    def draw(self, events, mouse) -> None:
        if not self.should_draw: return

        self._surface.fill(WHITE)

        self._controls(events, mouse)
        self._controls_settings_main_menu(events, mouse)

        self._surface.blit(self._screen_width_text, (4, 0))
        self._surface.blit(self._screen_height_text, (4, 27))
        self._surface.blit(self._fullscreen_text, (4, 54))

        self._plus_screen_width = pygame.draw.rect(self._surface, RED, pygame.Rect(self.width - 25, 3, 22, 22), 2)
        self._surface.blit(font.departure_mono_size_22.render("+", False, RED), (self.width - 21, -1))
        self._minus_screen_width = pygame.draw.rect(self._surface, RED, pygame.Rect(self.width - 25 - 25, 3, 22, 22), 2)
        self._surface.blit(font.departure_mono_size_22.render("-", False, RED), (self.width - 21 - 25, -1))

        self._plus_screen_height = pygame.draw.rect(self._surface, RED, pygame.Rect(self.width - 25, 30, 22, 22), 2)
        self._surface.blit(font.departure_mono_size_22.render("+", False, RED), (self.width - 21, -1 + 27))
        self._minus_screen_height = pygame.draw.rect(self._surface, RED, pygame.Rect(self.width - 25 - 25, 30, 22, 22), 2)
        self._surface.blit(font.departure_mono_size_22.render("-", False, RED), (self.width - 21 - 25, -1 + 27))

        self._toggle_fullscreen = pygame.draw.rect(self._surface, RED, pygame.Rect(self.width - 25, 57, 22, 22), 2)
        if self._fullscreen_value: self._surface.blit(font.departure_mono_size_22.render("X", False, RED), (self.width - 21, 27 * 2))

        self._apply_button = pygame.draw.rect(self._surface, RED, pygame.Rect(4, 84, 75, 27), 2)
        self._surface.blit(font.departure_mono_size_22.render("Apply", False, RED), (6, 82))

        pygame.draw.rect(self._surface, RED, pygame.Rect(self.width - 300 - 4, 84, 300, 27), 2)
        self._set_screen_resolution_button = self._surface.blit(font.departure_mono_size_22.render("Set screen resolution", False, RED), (self.width - 300 - 2, 82))

        screen.blit(self._shadow.surface, (self.xy.x - self._shadow.radius, self.xy.y - self._shadow.radius))
        screen.blit(self._surface, self.xy)

    def _change_screen_width(self, value):
        self._screen_width_value = value
        self._screen_width_text = font.departure_mono_size_22.render(f"Screen width: {self._screen_width_value}", False, RED)

    def _change_screen_height(self, value):
        self._screen_height_value = value
        self._screen_height_text = font.departure_mono_size_22.render(f"Screen height: {self._screen_height_value}", False, RED)

    def _set_screen_resolution(self):
        self._screen_width_value, self._screen_height_value = pygame.display.get_desktop_sizes()[0]
        self._screen_width_text = font.departure_mono_size_22.render(f"Screen width: {self._screen_width_value}", False, RED)
        self._screen_height_text = font.departure_mono_size_22.render(f"Screen height: {self._screen_height_value}", False, RED)

    def _toggle_fullscreen_method(self):
        self._fullscreen_value = not self._fullscreen_value
        self._fullscreen_text = font.departure_mono_size_22.render(f"Fullscreen: {self._fullscreen_value}", False, RED)

    def _apply_method(self):
        settings.screen_width, settings.screen_height = self._screen_width_value, self._screen_height_value
        resize_screen(settings.screen_width, settings.screen_height)

        if settings.fullscreen != self._fullscreen_value:
            settings.fullscreen = self._fullscreen_value
            pygame.display.toggle_fullscreen()

        self.should_draw = False

settings_menu = Settings(None, 400, 82 + 27 + 5)
floating_windows.append(settings_menu)
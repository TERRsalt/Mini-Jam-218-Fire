import pygame
import sys

from colors import *
from debug import debug_menu
from display import screen
from settings import screen_width
from clickable import clickables
from fonts import font
from main_menu.button import start_the_game, settings, quit_the_game
from text_funs import render_text_in_the_middle
from interval_time import interval
from music import music_player
from main_menu.settings_main_menu import settings_menu

class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

        self.game_running = True

        self.clock = pygame.time.Clock()
        self.fps = int(self.clock.get_fps())

        self._title = font.retron_2000_size_108.render("Welcome to H.E.L.L.", False, WHITE)
        self._y_for_the_title = 233
        self._should_title_go_up = False
        self._should_interval = True

    def run(self) -> None:
        self.clock = pygame.time.Clock()
        while self.game_running:
            self.clock.tick(60)
            self.fps = int(self.clock.get_fps())

            events = pygame.event.get()
            mouse = pygame.Vector2(pygame.mouse.get_pos())

            #info # Logic #

            clickables.clickables = []

            music_player.play_random_music(events)

            #info # Drawing the GUI #

            screen.fill(RED)

            if interval(250, "title") and self._should_interval:
                if self._should_title_go_up: self._y_for_the_title -= 1
                else: self._y_for_the_title += 1

                if self._y_for_the_title == 231 or self._y_for_the_title == 235: self._should_title_go_up = not self._should_title_go_up

            elif not interval(250, "title"): self._should_interval = True

            render_text_in_the_middle(self._title, screen, pygame.Vector2(0, self._y_for_the_title), screen_width)
            render_text_in_the_middle(self._title, screen, pygame.Vector2(0, self._y_for_the_title), screen_width)

            start_the_game.draw(150 + self._y_for_the_title)
            settings.draw(150 + self._y_for_the_title + 125)
            quit_the_game.draw(150 + self._y_for_the_title + 125 * 2)

            settings_menu.draw(events, mouse)

            debug_menu.draw(events, f"FPS: {self.fps}")

            #info # Controls #

            for event in events:
                if event.type == pygame.QUIT: self._quit_the_game()

                elif event.type == pygame.MOUSEBUTTONUP:
                    if start_the_game.rect.collidepoint(mouse): clickables.add(10, lambda: self._change_scene_to_desk(), "click")

                    elif settings.rect.collidepoint(mouse): clickables.add(10, lambda: self._settings_menu_method(), "click")

                    elif quit_the_game.rect.collidepoint(mouse): clickables.add(10, lambda: self._quit_the_game(), "click")

            clickables.process_clickables()

            #info # Rendering stuff onto the screen #

            pygame.display.flip()

    def _change_scene_to_desk(self):
        self.game_running = False
        self.game_state_manager.current_class = "desk"

    @staticmethod
    def _settings_menu_method(): settings_menu.should_draw = not settings_menu.should_draw

    @staticmethod
    def _quit_the_game():
        pygame.quit()
        sys.exit()
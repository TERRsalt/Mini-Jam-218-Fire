import pygame
import sys
import random

from desk.heaven_desk import heaven
from desk.mini_desk import mini_desk_instance
from desk.timer import timer_instance
from desk.world import world_instance, SylwesterLook
from colors import *
from debug import debug_menu
from display import screen, screen_width
from clickable import clickables
from desk.document import reset_day
import desk.document as document
from floating_window import floating_windows
from desk.furnace_desk import furnace
from desk.desk_desk import desk_instance
from desk.days import *
from fonts import font
from text_funs import render_text_in_the_middle
from interval_time import previous_times

class Desk:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.gameStateManager = game_state_manager

        self.game_running = True

        self.clock = pygame.time.Clock()
        self.fps = int(self.clock.get_fps())

        #info # Stuff for the days #

        self._game_lost = None
        self._day_complete = False

        self._sylwester_talking = True

        self._number_of_burned_documents = 0

        reset_day()

    def run(self) -> None:
        self.clock = pygame.time.Clock()
        while self.game_running:
            self.clock.tick(60)
            self.fps = int(self.clock.get_fps())

            events = pygame.event.get()
            mouse = pygame.Vector2(pygame.mouse.get_pos())

            #info # Logic #

            clickables.clickables = []

            #minor # Losing the game #

            if furnace.temperature < 555: self._game_lost = "low_temperature"
            elif furnace.temperature > 777: self._game_lost = "high_temperature"

            elif timer_instance.times_up: self._game_lost = "time"

            elif global_dictionary["mistakes"] > 0: self._game_lost = "mistakes"

            #minor # Wining the game #

            if global_dictionary["burned_documents"] >= documents_to_burn[global_dictionary["days"] - 1] and \
                    furnace.temperature_minus_change == 0 and furnace.temperature_plus_change == 0:
                for document_single in document.documents:
                    if document_single.sum_of_sins != 0 and document_single.look.rect.colliderect(heaven.rect):
                        global_dictionary["mistakes"] += 1
                    elif document_single.sum_of_sins == 0 and not document_single.look.rect.colliderect(heaven.rect):
                        global_dictionary["mistakes"] += 1

                    #elif document.sins.keys()

                #print(global_dictionary["mistakes"])
                #print(document.documents)
                if not global_dictionary["mistakes"] > 0: self._day_complete = True

            #info # Drawing the GUI #

            if self._game_lost is None and not self._day_complete:
                screen.fill(WHITE)

                heaven.draw()

                if dialogs[global_dictionary["days"] - 1].sylwester_talking:
                    furnace.draw(events, mouse, False)
                    world_instance.draw(SylwesterLook.SYLWESTER)
                    dialogs[global_dictionary["days"] - 1].draw(events, Voice.SYLWESTER)
                    timer_instance.draw(False)
                else:
                    furnace.draw(events, mouse)
                    world_instance.draw()
                    timer_instance.draw()

                mini_desk_instance.draw()
                desk_instance.draw()

                for floating_window in reversed(floating_windows.copy()): floating_window.draw(events, mouse)

            elif self._day_complete:
                screen.fill(YELLOW)
                text = font.retron_2000_size_108.render(f"Day {global_dictionary["days"]} complete", False, WHITE)
                render_text_in_the_middle(text, screen, pygame.Vector2(0, 444), screen_width)
                self._day_complete = False
                self._game_lost = None
                global_dictionary["days"] += 1
                pygame.display.flip()
                pygame.time.wait(3000)
                previous_times["furnace"] = pygame.time.get_ticks()
                reset_day()
            elif self._game_lost is not None:
                screen.fill(RED)
                text = font.retron_2000_size_108.render(f"You lost", False, WHITE)
                render_text_in_the_middle(text, screen, pygame.Vector2(0, 444), screen_width)
                self._day_complete = False
                self._game_lost = None
                pygame.display.flip()
                pygame.time.wait(3000)
                previous_times["furnace"] = pygame.time.get_ticks()
                reset_day()

            debug_menu.draw(events, f"FPS: {self.fps}")

            #info # Controls #

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            clickables.process_clickables()

            #info # Rendering stuff onto the screen #

            pygame.display.flip()
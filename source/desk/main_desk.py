import pygame
import sys
import random

from desk.heaven_desk import heaven
from desk.mini_desk import mini_desk_instance
from desk.timer import timer_instance
from desk.world import world_instance, SylwesterLook
from colors import *
from debug import debug_menu
from display import screen
from clickable import clickables
from desk.document import reset_day
from floating_window import floating_windows
from desk.furnace_desk import furnace
from desk.desk_desk import desk_instance
from desk.days import *

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
        self._day = 1

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

            #minor # Wining the game #

            if self._number_of_burned_documents >= documents_to_burn[self._day - 1]:
                if furnace.temperature + furnace.planned_temperature < 555: self._game_lost = "low_temperature"
                elif furnace.temperature + furnace.planned_temperature > 777: self._game_lost = "high_temperature"
                self._day_complete = True

            #info # Drawing the GUI #

            if not self._game_lost:
                screen.fill(WHITE)

                heaven.draw()

                if dialogs[self._day - 1].sylwester_talking:
                    furnace.draw(events, mouse, False)
                    world_instance.draw(SylwesterLook.SYLWESTER)
                    dialogs[self._day - 1].draw(events, Voice.SYLWESTER)
                    timer_instance.draw(False)
                else:
                    furnace.draw(events, mouse)
                    world_instance.draw()
                    timer_instance.draw()

                mini_desk_instance.draw()
                desk_instance.draw()

                for floating_window in reversed(floating_windows.copy()): floating_window.draw(events, mouse)

            else: screen.fill(RED)

            debug_menu.draw(events, f"FPS: {self.fps}")

            #info # Controls #

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            clickables.process_clickables()

            #info # Rendering stuff onto the screen #

            pygame.display.flip()
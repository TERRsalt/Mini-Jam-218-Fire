import pygame
import sys

from desk.dialog import Voice, dialog_1, Dialog
from desk.heaven_desk import heaven
from desk.mini_desk import mini_desk_instance
from desk.timer import timer_instance
from desk.world import world_instance, SylwesterLook
from colors import *
from debug import debug_menu
from display import screen
from clickable import clickables
from floating_window import floating_windows

from desk.furnace_desk import furnace
from desk.desk_desk import desk_instance

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

        self._number_of_documents_to_burn = 10
        self._message_1 = [
        #     "Hi! I'm Sylwester!",
        #     "I'm the boss here",
        #     "This place is called H.E.L.L.",
        #     "You can call me also the Devil",
        #     "You were sentenced here...",
        #     "for the eternity",
        #     "But lucky you...",
        #     "...I have chosen YOU...",
        #     "...to serve as my worker in...",
        #     "...H.E.L.L. bureaucracy",
        #     "See this furnace on you right?",
        #     "You wanna keep it at 666°C",
        #     "If it drops below 555°C...",
        #     "...then you will be...",
        #     "...fired and sent...",
        #     "...back to literal hell",
        #     "But if it ever goes...",
        #     "...above 777°C...",
        #     "...then it potentially...",
        #     "...may explode",
        #     "Why 777°C?",
        #     "Well we order it from..",
        #     "H.E.A.V.E.N. and it's Mireks's...",
        #     "...I mean God's...",
        #     "...favorite number...",
        #     "...or something",
        #     "Either way you...",
        #     "...don't wanna to go...",
        #     "...above this temperature...",
        #     "...because if you do...",
        #     "...then I will guarantee more...",
        #     "...suffering to you",
        #     "Got it? Good",
        #     "So for the first day...",
        #     "...I don't have any...",
        #     "...special requests",
        #     "You just need to burn...",
        #     f"...{self._number_of_documents_to_burn} documents before...",
        #     "the time runs out",
        #     "And remember that the...",
        #     "...documents with only...",
        #     "...virtues should be sent",
        #     "...to H.E.A.V.E.N",
        #     "They were lost...",
        #     "...somewhere in our...",
        #     "...bureaucracy",
        #     "You will have only...",
        #     "3 mistakes, before...",
        #     "...I will come",
        #     "So good luck in your...",
            "...new eternal work!"
        ]
        self._dialog_1 = Dialog(self._message_1, Voice.SYLWESTER)

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

            if self._number_of_burned_documents >= self._number_of_documents_to_burn: self._day_complete = True

            #info # Drawing the GUI #

            screen.fill(WHITE)

            heaven.draw()

            if self._dialog_1.sylwester_talking:
                furnace.draw(events, mouse, False)
                world_instance.draw(SylwesterLook.SYLWESTER)
                self._dialog_1.draw(events, Voice.SYLWESTER)
                timer_instance.draw(False)
            else:
                furnace.draw(events, mouse)
                world_instance.draw()
                timer_instance.draw()

            mini_desk_instance.draw()
            desk_instance.draw()

            for floating_window in reversed(floating_windows.copy()): floating_window.draw(events, mouse)

            debug_menu.draw(events, f"FPS: {self.fps}")

            #info # Controls #

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            clickables.process_clickables()

            #info # Rendering stuff onto the screen #

            pygame.display.flip()
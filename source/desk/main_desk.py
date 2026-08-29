import pygame
import sys

from desk.dialog import dialog_1
from desk.heaven_desk import heaven
from desk.mini_desk import mini_desk_instance
from desk.timer import timer_instance
from desk.world import world_instance
from interval_time import interval
from colors import *
from debug import debug_menu
from display import screen, screen_width, screen_height
from clickable import clickables
from floating_window import floating_windows

from desk.document import documents
from desk.furnace_desk import furnace
from desk.desk_desk import desk_instance

class Desk:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.gameStateManager = game_state_manager

        self.initialized = False
        self.game_running = True

        self.clock = pygame.time.Clock()
        self.fps = int(self.clock.get_fps())

    def _start(self) -> None:
        self.initialized = True

    def run(self) -> None:
        if not self.initialized:
            self._start()
            self.initialized = True

        self.clock = pygame.time.Clock()
        while self.game_running:
            self.clock.tick(60)
            self.fps = int(self.clock.get_fps())

            events = pygame.event.get()
            mouse = pygame.Vector2(pygame.mouse.get_pos())

            #info # Logic #

            clickables.clickables = []

            #info # Drawing the GUI #

            screen.fill(WHITE)

            heaven.draw()
            furnace.draw(events, mouse)
            world_instance.draw()
            mini_desk_instance.draw()
            timer_instance.draw()

            dialog_1.draw(events)

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
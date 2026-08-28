import pygame
import sys

from desk.furnace_desk import furnace
from interval_time import interval
from colors import *
from debug import debug_menu
from desk.document import documents
from display import screen, screen_width, screen_height
from clickable import clickables

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

            pygame.draw.rect(screen, PURPLE, pygame.Rect(0, 0, 400, screen_height))
            pygame.draw.rect(screen, RED, pygame.Rect(400, 0, 1100, screen_height))

            furnace.draw(events, mouse)

            for i in range(len(documents)): documents[i].draw(events, mouse)

            debug_menu.draw(events, f"FPS: {self.fps}")

            #info # Controls #

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            clickables.process_clickables()

            #info # Rendering stuff onto the screen #

            pygame.display.flip()
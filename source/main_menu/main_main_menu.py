import pygame
import sys

from colors import *
from debug import debug_menu
from display import screen
from clickable import clickables

class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.gameStateManager = game_state_manager

        self.game_running = True

        self.clock = pygame.time.Clock()
        self.fps = int(self.clock.get_fps())

    def run(self) -> None:
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

            debug_menu.draw(events, f"FPS: {self.fps}")

            #info # Controls #

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            clickables.process_clickables()

            #info # Rendering stuff onto the screen #

            pygame.display.flip()
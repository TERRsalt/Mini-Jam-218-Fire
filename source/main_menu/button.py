import pygame

from display import screen
from settings import screen_width
from colors import *
from fonts import font
from text_funs import render_text_in_the_middle

class Button:
    def __init__(self, text):
        self._width, self._height = 666, 104
        self._xy = pygame.Vector2(screen_width // 2 - self._width // 2, 0)

        self._surface = pygame.Surface((self._width, self._height)).convert_alpha()
        self._surface.fill(TRANSPARENT)
        pygame.draw.rect(self._surface, WHITE, pygame.Rect(0, 0, self._width, self._height), 3)

        self.rect = pygame.Rect(self._xy.x, self._xy.y, self._width, self._height)

        self._text = font.retron_2000_size_54.render(text, False, WHITE)
        render_text_in_the_middle(self._text, self._surface, pygame.Vector2(0, 47), self._width)

    def draw(self, y) -> None:
        screen.blit(self._surface, (self._xy.x, y))
        self.rect = pygame.Rect(self._xy.x, y, self._width, self._height)

start_the_game = Button("Start the game")
settings = Button("Settings")
quit_the_game = Button("Quit")
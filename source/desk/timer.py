import pygame

from desk.world import world_instance
from display import screen
from colors import *
from interval_time import interval, previous_times
from fonts import font

class Timer:
    def __init__(self):
        self.minutes = 5
        self.seconds = 0
        self.time_in_seconds = self.minutes * 60 + self.seconds
        self.times_up = False

        self._image = pygame.image.load("assets/gfx/timer.png").convert_alpha()
        self._width, self._height = self._image.get_width(), self._image.get_height()
        self._xy = pygame.Vector2(19, world_instance.height - self._height - 10)
        self._rect = pygame.Rect(self._xy.x, self._xy.y, self._width, self._height)

    def _run(self):
        if interval(1000, "timer"):
            self.seconds -= 1
            if self.seconds < 0:
                self.seconds = 59
                self.minutes -= 1
            self.time_in_seconds -= 1

        if self.time_in_seconds <= 0:
            self.minutes = self.seconds = 0
            self.times_up = True

    def draw(self, should_time_go = True):
        if should_time_go: self._run()
        else: previous_times["timer"] = pygame.time.get_ticks()

        screen.blit(self._image, self._xy)
        time_minutes_seconds = font.departure_mono_size_22.render(f"{self.minutes:02d}:{self.seconds:02d}", False, RED)
        screen.blit(time_minutes_seconds, (self._xy.x + 8, self._xy.y + 7))

timer_instance = Timer()
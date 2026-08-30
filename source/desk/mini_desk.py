import pygame

from clickable import clickables
from colors import *
from display import screen
from music import music_player
from settings import screen_height
from shadow import Shadow

from desk.world import world_instance

class MiniDesk:
    def __init__(self):
        self.width, self.height = world_instance.width, screen_height - world_instance.height
        self.y = screen_height - self.height
        self._rect = pygame.Rect(0, self.y, self.width, self.height)

        self._border_top_left_surface = pygame.Surface((self.width, 3)).convert()
        self._border_top_left_surface.fill(YELLOW)
        self._shadow_border_top_left = Shadow(self._border_top_left_surface)

        self._music_xy = pygame.Vector2(self.width - 248, self.y + 10)
        self._music_rect = pygame.Rect(self._music_xy.x, self._music_xy.y, 240, 186)
        self._music_playing_image = pygame.image.load("assets/gfx/music_playing.png")
        self._music_stopped_image = pygame.image.load("assets/gfx/music_stopped.png")

    def _controls(self, events, mouse):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self._music_rect.collidepoint(mouse):
                clickables.add(10, lambda: self._toggle_music(), "click")

    def draw(self, events, mouse):
        self._controls(events, mouse)

        pygame.draw.rect(screen, RED, self._rect)

        screen.blit(self._shadow_border_top_left.surface, (-self._shadow_border_top_left.radius, self.y - self._shadow_border_top_left.radius))
        screen.blit(self._border_top_left_surface, (0, self.y))

        if music_player.should_play: screen.blit(self._music_playing_image, self._music_xy)
        else: screen.blit(self._music_stopped_image, self._music_xy)

    @staticmethod
    def _toggle_music(): music_player.should_play = not music_player.should_play

mini_desk_instance = MiniDesk()
import pygame

from colors import *
from display import screen, screen_width, screen_height
from interval_time import interval
from fonts import font
from shadow import Shadow
from floating_window import floating_windows

from desk.document import documents

class Furnace:
    def __init__(self):
        self.temperature = 666
        self.last_temperature = 666
        self.planned_temperature = 0
        self.temperature_change = 0

        self.width, self.height = 451, screen_height - 333
        self.xy = pygame.Vector2(screen_width - self.width, 0)

        self._surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self._surface.fill(YELLOW)

        self._border_surface = pygame.Surface((3, screen_height)).convert()
        self._border_surface.fill(WHITE)
        self._shadow_border = Shadow(self._border_surface)

        self._rect = pygame.Rect(self.xy.x, self.xy.y, self.width, self.height)

        self._surface_furnace = pygame.Surface((self.width, self.height)).convert_alpha() #minor # What a name #
        self._surface_furnace.fill(TRANSPARENT)
        self._image_furnace = pygame.image.load("assets/gfx/furnace.png").convert_alpha()
        self._image_chimney = pygame.image.load("assets/gfx/furnace_chimney.png").convert_alpha()
        self._surface_furnace.blit(self._image_furnace, (0, self.height - self._image_furnace.get_height()))
        y_chimney = self._image_furnace.get_height() - 40
        while y_chimney > -41:
            self._surface_furnace.blit(self._image_chimney, (0, y_chimney))
            y_chimney -= 40
        self._shadow_furnace = Shadow(self._surface_furnace)

        self._fires = [
            pygame.image.load("assets/gfx/furnace_fire_1.png").convert_alpha(),
            pygame.image.load("assets/gfx/furnace_fire_2.png").convert_alpha(),
            pygame.image.load("assets/gfx/furnace_fire_3.png").convert_alpha(),
            pygame.image.load("assets/gfx/furnace_fire_4.png").convert_alpha()
        ]
        self._shadow_fires = [
            Shadow(self._fires[0], color = YELLOW),
            Shadow(self._fires[1], color = YELLOW),
            Shadow(self._fires[2], color = YELLOW),
            Shadow(self._fires[3], color = YELLOW),
        ]
        self._fire_to_choose = -1


        width_minus_in_rect_furnace = self.width // 4
        self._rect_furnace = pygame.Rect(self.xy.x + width_minus_in_rect_furnace, self.xy.y, self.width + width_minus_in_rect_furnace, self.height)

    def _logic(self, events, mouse):
        if interval(500, "furnace"):
            if self.temperature_change == 0:
                if self.planned_temperature > 0: self.temperature_change = 1
                elif self.planned_temperature < 0: self.temperature_change = -1

            if self.planned_temperature != 0: self.planned_temperature -= self.temperature_change
            else: self.temperature_change = 0

            self.temperature += self.temperature_change - 1

            self._fire_to_choose += 1
            if self._fire_to_choose >= 4: self._fire_to_choose = 0

        document_to_delete = None
        for i in range(len(documents)):
            if documents[i].look.rect.colliderect(self._rect_furnace):
                self.planned_temperature += documents[i].sum_of_sins_and_virtues

                if documents[i].sum_of_sins_and_virtues > 0: self.temperature_change += 1
                else: self.temperature_change -= 1

                document_to_delete = i

        if document_to_delete is not None:
            deleted_document = documents.pop(document_to_delete)
            if deleted_document.look in floating_windows: floating_windows.remove(deleted_document.look)

    def draw(self, events, mouse):
        self._logic(events, mouse)

        screen.blit(self._surface, self.xy)

        #pygame.draw.rect(screen, PURPLE, self._rect_furnace)

        xy_for_the_fire = pygame.Vector2(self.xy.x + 75, self.height - 260)
        pygame.draw.rect(screen, RED, pygame.Rect(xy_for_the_fire.x, xy_for_the_fire.y, 300, 200))
        screen.blit(self._shadow_fires[self._fire_to_choose].surface,
                (xy_for_the_fire.x - self._shadow_fires[self._fire_to_choose].radius, xy_for_the_fire.y - self._shadow_fires[self._fire_to_choose].radius))
        screen.blit(self._fires[self._fire_to_choose], xy_for_the_fire)

        screen.blit(self._shadow_furnace.surface, (self.xy.x - self._shadow_furnace.radius,  -self._shadow_furnace.radius))
        screen.blit(self._surface_furnace, (self.xy.x, 0))

        screen.blit(font.retron_2000_size_27.render(f"Temperature: {self.temperature}", False, WHITE), (1600, 100))
        screen.blit(font.retron_2000_size_27.render(f"Planned: {self.planned_temperature}", False, WHITE), (1600, 200))
        screen.blit(font.retron_2000_size_27.render(f"Change: {self.temperature_change}", False, WHITE), (1600, 300))

        screen.blit(self._shadow_border.surface, (self.xy.x - 2 - self._shadow_border.radius, self.xy.y - self._shadow_border.radius))
        screen.blit(self._border_surface, (self.xy.x - 2, self.xy.y))

furnace = Furnace()
import pygame

from colors import *
from desk.days import global_dictionary
from display import screen, screen_width, screen_height
from interval_time import interval
from fonts import font
from shadow import Shadow
from floating_window import floating_windows, dragging

import desk.document as document

class Furnace:
    def __init__(self):
        self.temperature = 666
        self.last_temperature = 666

        self.planned_plus_temperature = 0
        self.temperature_plus_change = 0
        self.planned_minus_temperature = 0
        self.temperature_minus_change = 0

        self.width, self.height = 451, screen_height - 444
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
        y_chimney = self.height - self._image_furnace.get_height() - 40
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

        self._rect_furnace = pygame.Rect(self.xy.x + 75, self.height - 260, 300, 200)

    def _logic(self, events, mouse, should_temperature_change):
        if interval(500, "furnace"):
            if should_temperature_change:
                if self.planned_plus_temperature > 0: self.planned_plus_temperature -= self.temperature_plus_change
                else: self.temperature_plus_change = 0

                if self.planned_minus_temperature < 0: self.planned_minus_temperature -= self.temperature_minus_change
                else: self.temperature_minus_change = 0

                self.temperature += self.temperature_plus_change + self.temperature_minus_change - 1

            self._fire_to_choose += 1
            if self._fire_to_choose >= 4: self._fire_to_choose = 0

        document_to_delete = None
        for i in range(len(document.documents)):
            if document.documents[i].look.rect.colliderect(self._rect_furnace) and not dragging.currently_dragging:
                sum_of_all_sins_and_virtues = document.documents[i].sum_of_sins_and_virtues

                if sum_of_all_sins_and_virtues > 0:
                    self.planned_plus_temperature += sum_of_all_sins_and_virtues
                    self.temperature_plus_change += 2

                else:
                    self.planned_minus_temperature += sum_of_all_sins_and_virtues
                    self.temperature_minus_change -= 2

                document_to_delete = i

                global_dictionary["burned_documents"] += 1

                if document.documents[i].sum_of_sins == 0: global_dictionary["mistakes"] += 1

        if document_to_delete is not None:
            #document.deleted_documents.append(document_to_delete)
            deleted_document = document.documents.pop(document_to_delete)
            if deleted_document.look in floating_windows: floating_windows.remove(deleted_document.look)

    def draw(self, events, mouse, should_temperature_change = True):
        self._logic(events, mouse, should_temperature_change)

        screen.blit(self._surface, self.xy)

        xy_for_the_fire = pygame.Vector2(self.xy.x + 75, self.height - 260)
        pygame.draw.rect(screen, RED, pygame.Rect(xy_for_the_fire.x, xy_for_the_fire.y, 300, 200))
        screen.blit(self._shadow_fires[self._fire_to_choose].surface,
                (xy_for_the_fire.x - self._shadow_fires[self._fire_to_choose].radius, xy_for_the_fire.y - self._shadow_fires[self._fire_to_choose].radius))
        screen.blit(self._fires[self._fire_to_choose], xy_for_the_fire)

        screen.blit(self._shadow_furnace.surface, (self.xy.x - self._shadow_furnace.radius,  -self._shadow_furnace.radius))
        screen.blit(self._surface_furnace, (self.xy.x, 0))

        screen.blit(font.departure_mono_size_22.render(f"{self.temperature}°C", False, WHITE), (self.xy.x + 4, self.xy.y))

        #pygame.draw.rect(screen, PURPLE, self._rect_furnace)

        screen.blit(font.retron_2000_size_27.render(f"Planned: {self.planned_plus_temperature}, {self.planned_minus_temperature}", False, WHITE), (1600, 200))
        screen.blit(font.retron_2000_size_27.render(f"Change: {self.temperature_plus_change}, {self.temperature_minus_change}", False, WHITE), (1600, 300))

        screen.blit(self._shadow_border.surface, (self.xy.x - 2 - self._shadow_border.radius, self.xy.y - self._shadow_border.radius))
        screen.blit(self._border_surface, (self.xy.x - 2, self.xy.y))

furnace = Furnace()
import pygame

from PIL import Image, ImageFilter

from colors import *

class Shadow:
    def __init__(self, base_surface, color = RED, size_of_shadow = 3):
        self._size_of_shadow = size_of_shadow

        self.radius = self._size_of_shadow * 3

        self.surface = pygame.Surface((base_surface.get_width() + self.radius * 2, base_surface.get_height() + self.radius * 2)).convert_alpha()
        self.surface.fill(TRANSPARENT)

        self.surface.blit(base_surface, (self.radius, self.radius))
        self.surface.fill(color, special_flags = pygame.BLEND_RGB_MULT)

        self._blur()

    def _blur(self) -> None:
        size_in_px = self.surface.get_size()
        surface_bytes = pygame.image.tobytes(self.surface, "RGBA")

        pil_image = Image.frombytes("RGBA", size_in_px, surface_bytes)
        pil_image = pil_image.filter(ImageFilter.GaussianBlur(self._size_of_shadow))

        self.surface = pygame.image.frombytes(pil_image.tobytes(), size_in_px, "RGBA")
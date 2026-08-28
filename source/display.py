import pygame

from settings import screen_width, screen_height, fullscreen

screen = pygame.display.set_mode((screen_width, screen_height))
if fullscreen: pygame.display.toggle_fullscreen()
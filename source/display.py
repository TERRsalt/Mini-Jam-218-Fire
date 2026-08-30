import pygame
from settings import screen_width, screen_height, fullscreen

screen = pygame.display.set_mode((screen_width, screen_height))
if fullscreen: pygame.display.toggle_fullscreen()

def resize_screen(new_width, new_height):
    global screen
    screen = pygame.display.set_mode((new_width, new_height))
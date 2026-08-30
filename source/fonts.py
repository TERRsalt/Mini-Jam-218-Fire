import pygame

class Fonts:
    def __init__(self):
        #info # Departure Mono (correct size n * 11) #

        self.departure_mono = "assets/fonts/departure_mono.otf"
        self.departure_mono_size_11 = pygame.font.Font("assets/fonts/departure_mono.otf", 11)
        self.departure_mono_size_22 = pygame.font.Font("assets/fonts/departure_mono.otf", 22)
        self.departure_mono_size_33 = pygame.font.Font("assets/fonts/departure_mono.otf", 33)

        #info # Retron2000 (correct size 2^n-1 * 27) #

        self.retron_2000 = "assets/fonts/retron_2000.ttf"
        self.retron_2000_size_14 = pygame.font.Font("assets/fonts/retron_2000.ttf", 14)
        self.retron_2000_size_20 = pygame.font.Font("assets/fonts/retron_2000.ttf", 20)
        self.retron_2000_size_27 = pygame.font.Font("assets/fonts/retron_2000.ttf", 27)
        self.retron_2000_size_54 = pygame.font.Font("assets/fonts/retron_2000.ttf", 54)
        self.retron_2000_size_108 = pygame.font.Font("assets/fonts/retron_2000.ttf", 108)

font = Fonts()
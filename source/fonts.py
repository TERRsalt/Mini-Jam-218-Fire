import pygame

class Fonts:
    def __init__(self):
        #info # Departure Mono (correct size n * 11) #

        self.departure_mono = "assets/fonts/departureMono.otf"
        self.departure_mono_size_11 = pygame.font.Font("assets/fonts/departureMono.otf", 11)
        self.departure_mono_size_22 = pygame.font.Font("assets/fonts/departureMono.otf", 22)
        self.departure_mono_size_33 = pygame.font.Font("assets/fonts/departureMono.otf", 33)

        #info # Retron2000 (correct size 2^n-1 * 27) #

        self.retron_2000 = "assets/fonts/retron2000.ttf"
        self.retron_2000_size_14 = pygame.font.Font("assets/fonts/retron2000.ttf", 14)
        self.retron_2000_size_20 = pygame.font.Font("assets/fonts/retron2000.ttf", 20)
        self.retron_2000_size_27 = pygame.font.Font("assets/fonts/retron2000.ttf", 27)
        self.retron_2000_size_54 = pygame.font.Font("assets/fonts/retron2000.ttf", 54)
        self.retron_2000_size_108 = pygame.font.Font("assets/fonts/retron2000.ttf", 108)

        #info # 712 Serif (correct size 16) #

        self.serif_712 = "assets/fonts/serif712.ttf"
        self.serif_712_size_16 = pygame.font.Font("assets/fonts/serif712.ttf", 16)

font = Fonts()
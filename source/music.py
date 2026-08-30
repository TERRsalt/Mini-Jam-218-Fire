import pygame
import os
import random

class Music:
    def __init__(self, music_folder = "assets/sfx/music", starting_music = "Shades of Spring.mp3"):
        self.music_folder = music_folder
        self._music = [file for file in os.listdir(music_folder) if file.endswith(".mp3")]
        self.should_play = True

        pygame.mixer.music.load(f"{self.music_folder}/{starting_music}")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

        self.MUSIC_END_EVENT = pygame.USEREVENT + 100
        pygame.mixer.music.set_endevent(self.MUSIC_END_EVENT)

    def play_random_music(self, events):
        if not self.should_play: return

        for event in events:
            if event.type == self.MUSIC_END_EVENT:
                pygame.mixer.music.load(f"{self.music_folder}/{random.choice(self._music)}")
                pygame.mixer.music.play()

music_player = Music()
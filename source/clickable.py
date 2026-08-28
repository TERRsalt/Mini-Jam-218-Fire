import pygame.mixer

class Clickable:
    def __init__(self): self.clickables = []

    def add(self, priority = 0, effect = None, sound = None) -> None:
        sound = f"assets/sfx/{sound}.ogg" if sound is not None else None
        self.clickables.append((priority, effect, sound))

    def process_clickables(self):
        if len(self.clickables) == 0: return

        self.clickables.sort()
        clickable = self.clickables[-1]
        if clickable[1] is not None: clickable[1]()
        if clickable[2] is not None: pygame.mixer.Sound(clickable[2]).play()

clickables = Clickable()
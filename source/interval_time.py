import pygame

previous_time = pygame.time.get_ticks()
def interval(interval_ms) -> bool:
    global previous_time

    current_time = pygame.time.get_ticks()
    if current_time - previous_time >= interval_ms:
        previous_time += interval_ms
        return True
    else: return False
import pygame

_previous_times = {"furnace": 0, "timer": 0}
def interval(interval_ms, key) -> bool:
    current_time = pygame.time.get_ticks()

    if current_time - _previous_times[key] >= interval_ms:
        _previous_times[key] += interval_ms
        return True
    else: return False
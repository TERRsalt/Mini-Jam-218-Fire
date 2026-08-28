import pygame

from colors import *

#info # `render_text_in_the_middle` #

def render_text_in_the_middle(rendered_text, surface, xy, width, should_draw_debug_rect_in_the_background = False) -> None:
    invisible_rect = pygame.Rect(xy.x, xy.y, width, 0)

    if should_draw_debug_rect_in_the_background:
        invisible_rect.height = 5
        pygame.draw.rect(surface, PURPLE, invisible_rect)

    surface.blit(rendered_text, rendered_text.get_rect(center = (invisible_rect.centerx, xy.y)))

#info # `render_text_with_outline` #

_circle_points_cache = {}
def _circle_points(radius) -> list[tuple[int, int]]: #exp # Giving the list of points around the original point #
    if radius in _circle_points_cache: return _circle_points_cache[radius]

    current_x, current_y = radius, 0
    decision_error = 1 - radius

    octant_points = []
    while current_x >= current_y:
        octant_points.append((current_x, current_y))
        current_y += 1

        if decision_error < 0: decision_error += 2 * current_y - 1
        else:
            current_x -= 1
            decision_error += 2 * (current_y - current_x) - 1

    all_points = list(octant_points)
    all_points += [(y, x) for x, y in octant_points if x > y] #exp # 2/8 done after this line #
    all_points += [(-x, y) for x, y in all_points if x] #exp # 4/8 done after this line #
    all_points += [(x, -y) for x, y in all_points if y] #exp # 8/8 done after this line #

    _circle_points_cache[radius] = all_points
    return all_points

def render_text_with_outline(font, text, antialias = False, color = WHITE, outline_color = BLACK, outline_width = 3) -> pygame.Surface:
    text_surface = font.render(text, antialias, color).convert_alpha()
    width = text_surface.get_width()
    height = text_surface.get_height()

    surface = pygame.Surface((width + 2 * outline_width, height + 2 * outline_width)).convert_alpha()
    surface.fill(TRANSPARENT)

    outline_surface = font.render(text, antialias, outline_color)
    #exp # Drawing the outline font `_circle_points(outline_width)` times around the original font #
    for delta_x, delta_y in _circle_points(outline_width): surface.blit(outline_surface, (delta_x + outline_width, delta_y + outline_width))

    surface.blit(text_surface, (outline_width, outline_width))
    return surface
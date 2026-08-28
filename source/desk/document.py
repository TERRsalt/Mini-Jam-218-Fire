import pygame

from colors import WHITE
from display import screen
from floating_window import FloatingWindow
from shadow import Shadow

_DICTIONARY_OF_ALL_SINS = {

}

class Document:
    def __init__(self):
        class DocumentDraw(FloatingWindow):
            def __init__(self, parent, xy, width, height):
                super().__init__(xy, width, height)
                self._parent = parent

                self._surface.fill(WHITE)

                self._shadow = Shadow(self._surface)

            def draw(self, events, mouse) -> None:
                if not self.should_draw: return

                self._controls(events, mouse)

                screen.blit(self._shadow.surface, (self._xy.x - self._shadow.radius, self._xy.y - self._shadow.radius))
                screen.blit(self._surface, self._xy)

        self._look = DocumentDraw(self, None, 300, 300)

    def draw(self, events, mouse) -> None: self._look.draw(events, mouse)

test_document = Document()
import pygame

from display import screen

if __name__ == "__main__":
    pygame.display.set_caption("Mini Jam 218: Fire")

    from game_class_manager import GameClassManager

    class Game:
        def __init__(self):
            pygame.mixer.init()
            pygame.font.init()

            self.screen = screen

            self.gameClassManager = GameClassManager("desk")

            self.scenes = {}

        def _import_scene(self, scene):
            if scene == "desk":
                from desk.main_desk import Desk
                self.scenes["desk"] = Desk(self.screen, self.gameClassManager)

        def run(self):
            pygame.event.get()

            while True:
                self._import_scene(self.gameClassManager.current_class)
                self.scenes[self.gameClassManager.current_class].run()

    game = Game()
    game.run()
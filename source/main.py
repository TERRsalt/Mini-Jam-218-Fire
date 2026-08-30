import pygame

from display import screen

if __name__ == "__main__":
    pygame.display.set_caption("Welcome to H.E.L.L.")

    from game_class_manager import GameClassManager

    class Game:
        def __init__(self):
            pygame.mixer.init()
            pygame.font.init()

            self.screen = screen

            self.gameClassManager = GameClassManager("main_menu")
            #self.gameClassManager = GameClassManager("desk")

            self.scenes = {}

        def _import_scene(self, scene):
            if scene == "main_menu":
                from main_menu.main_main_menu import MainMenu
                self.scenes["main_menu"] = MainMenu(self.screen, self.gameClassManager)

            elif scene == "desk":
                from desk.main_desk import Desk
                self.scenes["desk"] = Desk(self.screen, self.gameClassManager)

        def run(self):
            pygame.event.get()

            while True:
                self._import_scene(self.gameClassManager.current_class)
                self.scenes[self.gameClassManager.current_class].run()

    game = Game()
    game.run()
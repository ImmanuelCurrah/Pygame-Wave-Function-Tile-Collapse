import pygame

class Window:
    showWindow: bool = True

    def handleWindow(self, pygameEvent):
        for event in pygameEvent:
            if event.type == pygame.QUIT:
                self.__setWindow(False)

    def __setWindow(self, open: bool):
        self.showWindow = open

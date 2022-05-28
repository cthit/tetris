import pygame
from view.components.BaseTetromino import BaseTetromino
from config import SCREENSIZE, BACKGROUND_COLOUR, SCREEN_NAME
from controller.Observer import Observer

class View(Observer):
    def __init__(self, sprites_list):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.bg_colour = BACKGROUND_COLOUR
        self.sprites = sprites_list
        pygame.display.set_caption(SCREEN_NAME)
        pygame.display.update()

    def update(self):
        self.sprites.update()
        self.updateScreen()
    def updateScreen(self):
        self.screen.fill(self.bg_colour)
        self.sprites.draw(self.screen)
        pygame.display.update()


    def pressed(self,keys):
        self.sprites.update(keys)

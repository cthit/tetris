import pygame
from view.components.Button import Button
from config import SCREENSIZE, BACKGROUND_COLOUR, SCREEN_NAME

class View:
    def __init__(self, sprites_list):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.bg_colour = BACKGROUND_COLOUR
        self.sprites = sprites_list
        pygame.display.set_caption(SCREEN_NAME)
        pygame.display.update()

    def update(self):
        # send events to controller
        shouldContinueRunning = True
        self.screen.fill(self.bg_colour)
        self.screen.blit(pygame.image.load(
            r'resources/images/logo.png'), (SCREENSIZE[0]/2-200, 0))
        self.sprites.draw(self.screen)
        pygame.display.update()
        return shouldContinueRunning

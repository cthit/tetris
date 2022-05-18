import pygame


class View:
    def __init__(self, SCREENSIZE, BACKGROUD_COLOUR, SCREEN_NAME, sprites_list):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.bg_colour = BACKGROUD_COLOUR
        self.sprites = sprites_list
        pygame.display.set_caption(SCREEN_NAME)

        pygame.display.update()

    def update(self):
        # send events to controller
        shouldContinueRunning = True
        self.screen.fill(self.bg_colour)
        self.screen.blit(pygame.image.load(
            r'resources/images/logo.png'), (100, 100))
        pygame.display.update()
        return shouldContinueRunning

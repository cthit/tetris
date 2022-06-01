import pygame
from view.components.BaseTetromino import BaseTetromino,dir
from config import SCREENSIZE, BACKGROUND_COLOUR, SCREEN_NAME,RUNNING,U_FREQUENCY
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
        self.MOVE_DOWN=pygame.USEREVENT+1
        self.timer=pygame.time.set_timer(self.MOVE_DOWN,U_FREQUENCY)

    def update(self):
        self.updateScreen()
        self.getInput()

    def updateScreen(self):
        self.screen.fill(self.bg_colour)
        self.sprites.draw(self.screen)
        pygame.display.update()

    def getInput(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUNNING = False
                    if event.key == pygame.K_LEFT:
                        self.sprites.update(dir.LEFT)
                    if event.key == pygame.K_RIGHT:
                        self.sprites.update(dir.RIGHT)
                    if event.key == pygame.K_DOWN:
                        self.sprites.update(dir.DOWN)
                    if event.key == pygame.K_UP:
                        self.sprites.update(dir.UP)
                if event.type == self.MOVE_DOWN:
                    self.sprites.update(dir.DOWN)
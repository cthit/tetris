import pygame
from view.components.BaseTetromino import BaseTetromino, dir
from config import SCREENSIZE, BACKGROUND_COLOUR, SCREEN_NAME, U_FREQUENCY, WIDTH
from controller.Observer import Observer


class View(Observer):

    def __init__(self, running, sprites_list):
        pygame.init()
        pygame.font.init()
        self.running = running
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.bg_colour = BACKGROUND_COLOUR
        self.sprites = sprites_list
        self.current=BaseTetromino((WIDTH / 2 + 1, 0), [(0, 0), (1, 0), (2, 0), (2, 2)],
                      (3, 2))
        self.sprites.add(self.current)
        pygame.display.set_caption(SCREEN_NAME)
        pygame.display.update()
        self.MOVE_DOWN = pygame.USEREVENT + 1
        self.timer = pygame.time.set_timer(self.MOVE_DOWN, U_FREQUENCY)

    def update(self):
        self.updateScreen()
        self.getInput()
        self.checkTetromino()

    def updateScreen(self):
        self.screen.fill(self.bg_colour)
        self.sprites.draw(self.screen)
        pygame.display.update()

    def getInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running[0] = False
            if event.type == pygame.KEYDOWN:
                self.checkKeys(event)
            if event.type == self.MOVE_DOWN:
                self.sprites.update(dir.DOWN)

    def checkTetromino(self):
        if self.current.locked:
            self.sprites.remove(self.current)
            self.current=BaseTetromino((WIDTH / 2 + 1, 0), [(0, 0), (1, 0), (2, 0), (2, 2)],
                      (3, 2))
            self.sprites.add(self.current)

    def checkKeys(self,event):
        if event.key == pygame.K_ESCAPE:
            self.running[0] = False
        if event.key == pygame.K_LEFT:
            self.sprites.update(dir.LEFT)
        if event.key == pygame.K_RIGHT:
            self.sprites.update(dir.RIGHT)
        if event.key == pygame.K_DOWN:
            self.sprites.update(dir.DOWN)
        if event.key == pygame.K_UP:
            self.sprites.update(dir.UP)
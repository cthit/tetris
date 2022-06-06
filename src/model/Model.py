import pygame
from model.Playfield import Playfield
from view.View import View
from controller.Observer import Observer
from enum import Enum
import pygame

class state(Enum):
    EMPTY=0
    FILLED=1
class Model():

    def __init__(self, running, game_view=View(None, pygame.sprite.Group())) -> None:
        self.playfield: Playfield = Playfield()
        self.observers: list[Observer] = [game_view]
        self.running = running
        self.board=[[state.EMPTY]*20]*10

    def update(self) -> bool:
        while (self.running[0]):
            for observer in self.observers:
                observer.update()
            #time.sleep(1/FPS)

    def checkCollision(self,tetromino:list):
        for b in tetromino:
            if self.board[b[0],b[1]]==state.FILLED:
                return True
        return False

    def addBlob(self,tetromino:list):
        for b in tetromino:
            self.board[b[0],b[1]]=state.FILLED

    def checkLines(self):
        print(self.board)
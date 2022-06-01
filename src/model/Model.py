import pygame
from model.Playfield import Playfield
from view.View import View
from controller.Observer import Observer

class Model():
    def __init__(self,running,game_view=View(None,None)) -> None:
        self.playfield: Playfield = Playfield()
        self.observers:list[Observer]= [game_view]
        self.running=running

    def update(self) -> bool:
        while(self.running[0]):
            for observer in self.observers:
                observer.update()
            #time.sleep(1/FPS)

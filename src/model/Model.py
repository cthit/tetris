import pygame
from model.Playfield import Playfield
from view.View import View
from controller.Observer import Observer

class Model():
    def __init__(self,game_view=View(None)) -> None:
        self.playfield: Playfield = Playfield()
        self.observers:List[Observer]= [game_view]

    def update(self) -> bool:
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for observer in self.observers:
                observer.update()
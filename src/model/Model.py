import pygame
from model.Playfield import Playfield
from view.View import View

class Model():
    def __init__(self,game_view=View((100,100),(255,255,255),"Error",None)) -> None:
        self.playfield: Playfield = Playfield()
        self.game_view: View = game_view

    def run(self):
        running: bool = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.game_view.update()

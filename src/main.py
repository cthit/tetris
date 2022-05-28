import pygame
from config import *
from view.View import View
from model.Model import Model
from controller.Controller import Controller
from view.components.BaseTetromino import BaseTetromino


def main():
    list_of_sprites = pygame.sprite.Group()
    list_of_sprites.add(BaseTetromino("Test", (100, 100), (300, 300)))
    game_view = View(list_of_sprites)
    game_model = Model(game_view)
    game_controller = Controller(game_model)
    game_model.update()
    #game_controller.update()
    #game_controller.run()
    print("Okay, bye!\n👋")


if __name__ == "__main__":
    main()

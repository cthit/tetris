import pygame
from config import *
from view.View import View
from model.Model import Model


def main():
    list_of_sprites = None
    game_view = View(SCREENSIZE, BACKGROUND_COLOUR,
                     SCREEN_NAME, list_of_sprites)
    game_model = Model()
    isRunning = True
    while(isRunning):
        isRunning = game_view.update()
    game_model.run()


if __name__ == "__main__":
    main()

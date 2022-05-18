import pygame
from config import *
from view.View import View
from model.Model import Model


def main():
    list_of_sprites = None
    game_view = View(SCREENSIZE, BACKGROUND_COLOUR,
                     SCREEN_NAME, list_of_sprites)
    game_model = Model(game_view)

    game_model.run()
    print("Okay, bye!\n👋")


if __name__ == "__main__":
    main()

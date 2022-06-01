import pygame
from config import WIDTH
from view.View import View
from model.Model import Model
from controller.Controller import Controller
from view.components.BaseTetromino import BaseTetromino
from model.Playfield import Playfield


def main():
    running = [True]
    list_of_sprites = pygame.sprite.Group()
    list_of_sprites.add(
        BaseTetromino((WIDTH / 2 + 1, 0), [(0, 0), (1, 0), (2, 0), (2, 2)],
                      (3, 2)))
    list_of_sprites.add(Playfield())
    game_view = View(running, list_of_sprites)
    game_model = Model(running, game_view)
    game_model.update()
    print("Okay, bye!\n👋")


if __name__ == "__main__":
    main()

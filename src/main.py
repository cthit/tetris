import pygame
from config import *
from view.View import View
from model.Model import Model
from controller.Controller import Controller
from view.components.Button import Button
import _thread as tråd


def main():
    list_of_sprites = pygame.sprite.Group()
    list_of_sprites.add(Button("Test", (100, 100), (300, 300)))
    game_view = View(list_of_sprites)
    game_model = Model(game_view)
    game_controller = Controller()
    tråd.start_new_thread(game_model.run, ())
    print("test")
    game_controller.run()
    print("Okay, bye!\n👋")


if __name__ == "__main__":
    main()

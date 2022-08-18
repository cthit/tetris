from Game import Game
from TetrominoFactory import TetrominoFactory
import pygame

def tetris_loop():
	game=Game()
	game.main_loop()

if __name__ == '__main__':
	tetris_loop()
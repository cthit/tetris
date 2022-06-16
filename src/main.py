from Game import Game
from TetrominoFactory import TetrominoFactory
import pygame

def tetris_loop():
	game=Game()
	print(game.board)
	tetromino = TetrominoFactory.create_tetromino('J',0,0)
	for i in range(0, 4):
		for i in range(0, len(tetromino.get_tetromino())):
			print(tetromino.get_tetromino()[i])
		tetromino.rotate()


	




if __name__ == '__main__':
	tetris_loop()
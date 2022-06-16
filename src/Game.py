from random import randint
import pygame
from config import *
from enum import Enum
from TetrominoFactory import TetrominoFactory


class type(Enum):
	moving = 1
	static = 2
	empty = 3

class Game:
	def __init__(self):
		self.board=self.createBoard()
		pygame.init()
		self.screen=pygame.display.set_mode(SSIZE)
		pygame.display.set_caption("Tetris!")
		self.gClock=pygame.time.Clock()
		self.tick=0
		self.createTetromino()



	def createBoard(self):
		return [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

	def insertTetromino(self):
		pass

	def mainLoop(self):
		while True:
			self.getInput()
			self.tick+=1
			self.update()
			self.draw()
			self.gClock.tick(FRAMERATE)

	def deleteComplete(self):
		newBoard=[]
		for row in self.board:
			complete=True
			for block in row:
				if not block is type.static:
					complete=False
			if complete:
				newBoard.insert(0,[type.empty for x in range(WIDTH)])
			else:
				newBoard.append(row)

	def createTetromino(self):
		self.tetromino=TetrominoFactory.create_tetromino(TetrominoFactory.types[randint(0,len(TetrominoFactory.types))], 0, 0)

	def draw(self):
		# Draw screen background
		self.screen.fill(BLACK)

		# Draw tetromino

		# Draw static blocks
		for y in range(len(self.board)):
			for x in range(len(self.board[0])):
				if self.board[y][x] is type.static:
					pygame.draw.rect(self.screen, BLUE, (x*BLOCKSIZE, y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))

	def getInput(self):
		pass
	def moveDown(self):
		return True
	def update(self):
		if self.gClock.get_fps()/self.tick>FALLRATE:
			self.tick=0
			if not self.moveDown():
				self.insertTetromino()
				if not self.createTetromino():
					self.gameOver()

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
		tetro=self.tetromino.get_tetromino()
		baseX=self.tetromino.get_x()
		pass

	def mainLoop(self):
		while True:
			self.getInput()
			self.tick+=1
			self.checkTetromino()
			self.update()
			self.draw()
			#print(self.tetromino.get_coordinates())
			self.gClock.tick(FRAMERATE)

	def checkTetromino(self):
		pass

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
		#print(TetrominoFactory.types)
		self.tetromino=TetrominoFactory.create_tetromino(TetrominoFactory.types[randint(0,len(TetrominoFactory.types)-1)], 1, 4)
		return True

	def draw(self):
		# Draw screen background
		self.screen.fill(BLACK)

		# Draw tetromino
		(tetX,tetY)=self.tetromino.get_coordinates()
		shape=self.tetromino.get_tetromino()
		for y in range(len(shape)):
			for x in range(len(shape[y])):
				if(shape[y][x]) is 1:
					#print(tetX+x)
					pygame.draw.rect(self.screen,WHITE,[(tetX+x)*BLOCKSIZE,(tetY+y)*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE],0)



		# Draw static blocks
		for y in range(len(self.board)):
			for x in range(len(self.board[y])):
				if self.board[y][x] == 2:

					pygame.draw.rect(self.screen, BLUE, pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
		pygame.display.flip()

	def getInput(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key is pygame.K_ESCAPE:
					self.gameOver()
				else:
					self.tetromino.handle_keypress(event.key,self.board)

	def moveDown(self):
		return self.tetromino.move_down(self.board)

	def update(self):
		if self.tick>FRAMERATE*FALLRATE:
			self.tick=0
			if not self.moveDown():
				self.insertTetromino()
				if not self.createTetromino():
					self.gameOver()

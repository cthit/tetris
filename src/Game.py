from random import randint,shuffle
import pygame
from config import *
from enum import Enum
from TetrominoFactory import TetrominoFactory


class Game:
	def __init__(self):
		self.completed=0
		self.score=0
		self.board=self.createBoard()
		pygame.init()
		self.screen=pygame.display.set_mode(SSIZE)
		pygame.display.set_caption("Tetris!")
		self.gClock=pygame.time.Clock()
		self.tick=0
		self.reshuffleList()
		self.createTetromino()



	def createBoard(self):
		return [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

	def insertTetromino(self):
		tetro=self.tetromino.get_tetromino()
		color=self.tetromino.get_color()
		color=(color[0]-90,color[1]-90,color[2]-90)
		baseX=self.tetromino.get_x()
		baseY=self.tetromino.get_y()
		for y in range(len(tetro)):
			currY=baseY+y
			for x in range(len(tetro[y])):
				currX=baseX+x
				if tetro[y][x]==1:
					self.board[currY][currX]=color
		print(self.board)

	def mainLoop(self):
		while True:
			self.getInput()
			self.tick+=1
			self.update()
			self.draw()
			#print(self.tetromino.get_coordinates())
			self.gClock.tick(FRAMERATE)


	def deleteComplete(self):
		newBoard=[]
		completed=0
		if self.board[0][4]!=0:
			x=1/0
		for row in self.board:
			complete=True
			for block in row:
				if block ==0:
					complete=False
			if complete:
				newBoard.insert(0,[0 for i in range(WIDTH)])
				completed+=1
			else:
				newBoard.append(row)
		self.score+=POINTPERROW[completed%len(POINTPERROW)]
		if completed>0:
			self.completed+=1
		self.board=newBoard


	def createTetromino(self):
		#print(TetrominoFactory.types)
		if len(self.tetList)==0:
			self.reshuffleList()
		#self.tetromino=TetrominoFactory.create_tetromino(TetrominoFactory.types[randint(0,len(TetrominoFactory.types)-1)], 3, 0)
		self.tetromino=self.tetList.pop()
		return True

	def reshuffleList(self):
		self.tetList=[]
		for i in range(len(TetrominoFactory.types)):
			self.tetList.append(TetrominoFactory.create_tetromino(TetrominoFactory.types[i], 3, 0))
		shuffle(self.tetList)

	def draw(self):
		# Draw screen background
		self.drawScreen()
		# Draw tetromino
		self.drawTetromino()
		# Draw static blocks
		self.drawStaticBlocks()
		# Draw score
		self.drawScore()
		pygame.display.flip()

	def drawScreen(self):
		self.screen.fill(BLACK)
		for x in range(0, SWIDTH, BLOCKSIZE):
			for y in range(0, SHEIGHT, BLOCKSIZE):
				rect = pygame.Rect(x, y, BLOCKSIZE,BLOCKSIZE)
				pygame.draw.rect(self.screen, GRAY, rect, 1)

	def drawTetromino(self):
		tetroColor=self.tetromino.get_color()
		(tetX,tetY)=self.tetromino.get_coordinates()
		shape=self.tetromino.get_tetromino()
		for y in range(len(shape)):
			for x in range(len(shape[y])):
				if(shape[y][x]) is 1:
					#print(tetX+x)
					pygame.draw.rect(self.screen,tetroColor,[(tetX+x)*BLOCKSIZE,(tetY+y)*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE],0)

	def drawStaticBlocks(self):
		for y in range(len(self.board)):
			for x in range(len(self.board[y])):
				if self.board[y][x] != 0:

					pygame.draw.rect(self.screen, self.board[y][x], pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))

	def drawScore(self):
		font = pygame.font.SysFont(FONT, FONTSIZE)
		text = font.render("Score: " + str(self.score), True, WHITE)
		self.screen.blit(text, [0, 0])

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
		if self.tick>FRAMERATE*(FALLRATE/(1+self.completed*FALLINCREASE)):
			self.tick=0
			if not self.moveDown():
				self.insertTetromino()
				self.deleteComplete()
				if not self.createTetromino():
					self.gameOver()

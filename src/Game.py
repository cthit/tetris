from random import randint,shuffle
import pygame
from config import *
from enum import Enum
from TetrominoFactory import TetrominoFactory


class Game:
	def __init__(self):
		self.completed=0
		self.score=0
		self.board=self.create_board()
		pygame.init()
		self.screen=pygame.display.set_mode(SCREEN_SIZE)
		pygame.display.set_caption("Tetris!")
		self.clock=pygame.time.Clock()
		self.tick=0
		self.reshuffle_list()
		self.create_tetromino()



	def create_board(self):
		"""
		Creates a board with all blocks set to 0
		"""
		#TODO: implement this

	def insert_tetromino(self):
		"""
		Inserts the current tetromino into the board
		"""
		tetro=self.tetromino.get_tetromino()
		color=self.tetromino.get_color()
		color=(color[0]-90,color[1]-90,color[2]-90)
		base_x=self.tetromino.get_x()
		base_y=self.tetromino.get_y()
		for y in range(len(tetro)):
			curr_y=base_y+y
			for x in range(len(tetro[y])):
				curr_x=base_x+x
				if tetro[y][x]==1:
					self.board[curr_y][curr_x]=color

	def main_loop(self):
		"""
		Main game loop
		"""
		while True:
			self.get_input()
			self.tick+=1
			self.update()
			self.draw()
			self.clock.tick(FRAMERATE)


	def delete_complete(self):
		"""
		Deletes all complete rows
		"""
		new_board=[]
		completed=0
		for row in self.board:
			complete=True
			for block in row:
				if block ==0:
					complete=False
			if complete:
				new_board.insert(0,[0 for i in range(WIDTH)])
				completed+=1
			else:
				new_board.append(row)
		self.score+=POINT_PER_ROW[completed%len(POINT_PER_ROW)]
		if completed>0:
			self.completed+=1
		self.board=new_board


	def create_tetromino(self):
		"""
		Creates a new tetromino
		"""
		if len(self.tet_list)==0:
			self.reshuffle_list()
		self.tetromino=self.tet_list.pop()
		return True

	def reshuffle_list(self):
		"""
		Shuffles the tetromino list
		"""
		#TODO: implement this

	def draw(self):
		"""
		Draws the screen
		"""
		# Draw screen background
		self.draw_screen_background()
		# Draw tetromino
		self.draw_tetromino()
		# Draw static blocks
		self.draw_static_blocks()
		# Draw score
		self.draw_score()
		pygame.display.flip()

	def draw_screen_background(self):
		"""
		Draws the screen background
		"""
		self.screen.fill(BLACK)
		for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
			for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
				rect = pygame.Rect(x, y, BLOCK_SIZE,BLOCK_SIZE)
				pygame.draw.rect(self.screen, GRAY, rect, 1)

	def draw_tetromino(self):
		"""
		Draws the current tetromino"""
		tetro_color=self.tetromino.get_color()
		(tet_x,tet_y)=self.tetromino.get_coordinates()
		shape=self.tetromino.get_tetromino()
		for y in range(len(shape)):
			for x in range(len(shape[y])):
				if(shape[y][x]) is 1:
					pygame.draw.rect(self.screen,tetro_color,[(tet_x+x)*BLOCK_SIZE,(tet_y+y)*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE],0)

	def draw_static_blocks(self):
		"""
		Draws the static blocks
		"""
		#TODO: implement this

	def draw_score(self):
		"""
		Draws the score
		"""
		font = pygame.font.SysFont(FONT, FONT_SIZE)
		text = font.render("Score: " + str(self.score), True, WHITE)
		self.screen.blit(text, [0, 0])

	def get_input(self):
		"""
		Gets input from the user
		"""
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key is pygame.K_ESCAPE or event.type is pygame.QUIT:
					self.game_over()
				else:
					self.tetromino.handle_keypress(event.key,self.board)

	def move_down(self):
		"""
		Moves the tetromino down one row
		"""
		return self.tetromino.move_down(self.board)

	def game_over(self):
		"""
		Ends the game
		"""
		#TODO: implement this

	def should_game_quit(self):
		"""
		Checks if the game is filled to the top
		"""
		if self.board[0][4]!=0:
			self.game_over()

	def update(self):
		"""
		Updates game if new tick is reached
		"""
		if self.tick>FRAMERATE*(FALL_RATE/(1+self.completed*FALL_INCREASE)):
			self.tick=0
			if not self.move_down():
				self.insert_tetromino()
				self.should_game_quit()
				self.delete_complete()
				if not self.create_tetromino():
					self.game_over()

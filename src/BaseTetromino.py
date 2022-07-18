import pygame
from config import *
from random import randint
class BaseTetromino:
  """
  Base tetromino class, that contains shared logic for all tetrominoes.
  """

  def __init__(self, x: int, y: int, tetromino: list[list[int]]):
    self.__x = x
    self.__y = y
    self.__tetromino = tetromino.copy()
    self.color=(randint(100,255),randint(100,255),randint(100,255))

  def handle_keypress(self, key, board):
    if key is pygame.K_LEFT or key is pygame.K_a:
      self.move_left(board)
    elif key is pygame.K_RIGHT or key is pygame.K_d:
      self.move_right(board)
    elif key is pygame.K_DOWN or key is pygame.K_s:
      self.move_down(board)
    elif (key is pygame.K_UP) or (key is pygame.K_SPACE):
      self.rotate()

  def get_tetromino(self):
    """
    Dangerous: Returns a reference to the tetromino matrix.
    """
    return self.__tetromino

  def get_x(self):
    """
    Returns the x coordinate of the tetromino.
    """
    return self.__x

  def get_y(self):
    """
    Returns the y coordinate of the tetromino.
    """
    return self.__y

  def get_color(self):
    return self.color

  def get_coordinates(self):
    """
    Returns the coordinates of the tetromino in the form of a tuple of x and y.
    """
    return (self.__x, self.__y)

  def move_right(self,board):
    """
    Moves the tetromino one column to the right.
    """
    toMove=self.check_move_x(board,1)
    self.__x += toMove

  def move_left(self, board):
    """
    Moves the tetromino one column to the left.
    """
    toMove=self.check_move_x(board,-1)
    self.__x += toMove

  def check_move_x(self,board,toMove):
    figure=self.__tetromino
    for y in range(len(figure)):
      for x in range(len(figure[0])):
        print(f"y:{self.__y+y}, x:{self.__x+x+toMove}")
        if figure[y][x] == 1:
          if (self.__x+x+toMove<0) or (self.__x+x+toMove>=WIDTH):
            return 0
          if (board[self.__y+y][self.__x+x+toMove] != 0):
            return 0
    return toMove

  def check_move_y(self,board,toMove):
    figure=self.__tetromino
    for y in range(len(figure)):
      for x in range(len(figure[0])):
        if figure[y][x]==1:
          if (self.__y+y+toMove<0) or (self.__y+y+toMove>=HEIGHT):
            return False
          if (board[self.__y+y+toMove][self.__x+x] != 0):
            return False
    return True

  def move_down(self,board):
    """
    Moves the tetromino one row down.
    """
    if self.check_move_y(board,1):
      self.__y += 1
      return True
    return False

  def rotate(self):
    """
    Rotates the tetromino clockwise.
    """
    self.__tetromino = self.__rotate_clockwise(self.__tetromino)

  @staticmethod
  def __rotate_clockwise(tetromino: list[list[int]]):
    """
    Rotates the tetromino clockwise.
    """
    return list(zip(*tetromino[::-1]))

import pygame
from config import *
from random import randint
class BaseTetromino:
  """
  Base tetromino class, that contains shared logic for all tetrominoes.
  """

  def __init__(self, x: int, y: int, tetromino: list[list[int]]):
    """
    Initializes the tetromino.
    """
    self.__x = x
    self.__y = y
    self.__tetromino = tetromino.copy()
    self.color=(randint(150,255),randint(150,255),randint(150,255))

  def handle_keypress(self, key, board):
    """
    Handles the keypresses to move the tetromino.
    """
    #TODO: Implement this feature


  def get_tetromino(self):
    """
    Dangerous: Returns a reference to the tetromino matrix.
    """
    #TODO: Implement this feature

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
    toMove=self.can_move_x(board,1)
    self.__x += toMove

  def move_left(self, board):
    """
    Moves the tetromino one column to the left.
    """
    #TODO: Implement this feature

  def can_move_x(self,board,toMove):
    """
    Checks if possible to move the tetromino to the right or left.
    """
    #TODO: Implement this feature

  def can_move_down(self,board,toMove):
    """
    Checks if possible to move the tetromino down.
    """
    #TODO: Implement this feature

  def can_rotate(self,board):
    """
    Checks if possible to rotate the tetromino clockwise.
    """
    #TODO: this

  def move_down(self,board):
    """
    Moves the tetromino one row down.
    """
    if self.can_move_down(board,1):
      self.__y += 1
      return True
    return False

  def rotate(self, board):
    """
    Rotates the tetromino clockwise.
    """
    if self.can_rotate(board):
      self.__tetromino = self.__rotate_clockwise(self.__tetromino)
    return 0

  @staticmethod
  def __rotate_clockwise(tetromino: list[list[int]]):
    """
    Rotates the tetromino clockwise. Do not touch this function.
    """
    return list(zip(*tetromino[::-1]))

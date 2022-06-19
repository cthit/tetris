import pygame
class BaseTetromino:
  """
  Base tetromino class, that contains shared logic for all tetrominoes.
  """

  def __init__(self, x: int, y: int, tetromino: list[list[int]]):
    self.__x = x
    self.__y = y
    self.__tetromino = tetromino.copy()

  def handle_keypress(self, key, board):
    if key is pygame.K_LEFT:
      self.move_left(board)
    elif key is pygame.K_RIGHT:
      self.move_right(board)
    elif key is pygame.K_DOWN:
      self.move_down()
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
    for x in range(len(figure)):
      for y in range(len(figure)):
        if figure[x][y] == 1:
          if (board[self.__y+y][self.__x+x+toMove] == 1) or (self.__x+x+toMove<0):
            return 0
    return toMove

  def move_down(self):
    """
    Moves the tetromino one row down.
    """
    self.__y += 1

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

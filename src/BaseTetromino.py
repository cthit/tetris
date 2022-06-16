class BaseTetromino:
  """
  Base tetromino class, that contains shared logic for all tetrominoes.
  """

  def __init__(self, x: int, y: int, tetromino: list[list[int]]):
    self.__x = x
    self.__y = y
    self.__tetromino = tetromino.copy()

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

  def move_right(self):
    """
    Moves the tetromino one column to the right.
    """
    self.__x += 1

  def move_left(self):
    """
    Moves the tetromino one column to the left.
    """
    self.__x -= 1

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

  def __str__(self):
    return str(self.__tetromino)


  

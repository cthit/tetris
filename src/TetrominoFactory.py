from BaseTetromino import BaseTetromino

class TetrominoFactory:
	tetrominoes = {
		'I': [[1, 1, 1, 1],
					[0, 0, 0, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]],
		'J': [[1, 1, 1, 0],
					[0, 0, 1, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]],
		'L': [[0, 1, 1, 0],
					[0, 0, 1, 0],
					[0, 0, 1, 0],
					[0, 0, 0, 0]],
		'O': [[1, 1, 0],
					[1, 1, 0],
					[0, 0, 0],
					[0, 0, 0]],
		'S': [[0, 1, 1],
					[1, 1, 0],
					[0, 0, 0],
					[0, 0, 0]],
		'T': [[1, 1, 1],
					[0, 1, 0],
					[0, 0, 0],
					[0, 0, 0]],
		'Z': [[1, 1, 0],
					[0, 1, 1],
					[0, 0, 0],
					[0, 0, 0]]
	}

	@staticmethod
	def create_tetromino(tetromino_type: str, x: int, y: int):
		"""
		Creates a new tetromino of the given type.
		"""
		return BaseTetromino(x, y, TetrominoFactory.tetrominoes[tetromino_type])
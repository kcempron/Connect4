import numpy as np
import player as pl

# Provides the structure on which pieces are played within the constraints of the game.
class Board:
	# Visualize board as 2D Array.
	def __init__(self, row: int, col: int) -> None:
		self.board = Board.create_board(row, col)

	def clear_board(self) -> None:
		self.board = np.full_like(a = self.board, fill_value = "*")
		print("board cleared!")

	def set_piece(self, row: int, col: int) -> None:
		self.board[row, col] = "X"

	def get_board(self) -> np.ndarray:
		return self.board

	def __str__(self) -> str:
		return np.array2string(self.board)

	### Utility functions go here ###
	@staticmethod
	def create_board(row: int, col: int) -> np.ndarray:
		if row < 4 and col < 4:
			raise Exception("Board must have row or column size be a minimum of 4 to allow game.")
		else:
			print("board created!")
			return np.full(shape = (row, col), fill_value = "*", dtype = str)


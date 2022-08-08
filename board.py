import numpy as np
import player as pl

# Provides the structure on which pieces are played within the constraints of the game.
class Board:
	# Visualize board as 2D Array.
	def __init__(self, row: int, col: int) -> None:
		self.board = Board.create_board(row, col)
		self.row_length = row
		self.col_length = col

	def clear_board(self) -> None:
		self.board = np.full_like(a = self.board, fill_value = "*")
		print("board cleared!")

	def set_piece(self, row: int, col: int, player: pl.Player) -> None:
		self.board[row, col] = player.get_piece().name

	def get_piece(self, row: int, col: int) -> str:
		return self.board[row, col]

	def get_surr_row(self, row: int, col: int) -> list:
		left_four = (col - 3)
		start_index = left_four if left_four >= 0 else 0
		right_four = (col + 4)
		end_index = right_four if right_four <= self.col_length else self.col_length
		return self.board[row, start_index:end_index].tolist()

	def get_surr_col(self, row: int, col: int) -> list:
		top_four = (row - 3)
		start_index = top_four if top_four >= 0 else 0
		bot_four = (row + 4)
		end_index = bot_four if bot_four <= self.row_length else self.row_length
		return self.board[start_index:end_index, col].tolist()

	def get_diag_left(self, row: int, col: int) -> list:
		return self.board.diagonal(col - row).tolist()

	def get_diag_right (self, row: int, col: int) -> list:
		return np.fliplr(self.board).diagonal((self.col_length - col - 1) - row).tolist()

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


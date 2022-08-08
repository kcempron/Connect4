import board as b
import player as pl
import numpy as np

# Handles the state of the game and ensures that players are able to interact with the board within constraints.
class Game:
	def __init__(self, row: int, col: int, player_1_piece: pl.Piece, player_2_piece: pl.Piece) -> None:
		self.board = b.Board(row, col)
		self.player_1 = pl.Player(player_1_piece)
		self.player_2 = pl.Player(player_2_piece)
		self.players = {self.player_1, self.player_2}
		self.current_player = self.player_1
		self.game_started = False
		

	def start_game(self) -> None:
		self.game_started = True
		print("Time to start the game! Player_1 will start.")

	def reset_game(self) -> None:
		self.board.clear_board()
		self.game_started = False
		self.current_player = self.player_1
		print("Game has been reset")

	def set_piece(self, row: int, col: int) -> None:
		if (self.game_started == False):
			print("Game has not started. Please start game before setting pieces.")
			return None
		
		if (self.board.get_piece(row, col) != "*"):
			print("Board slot is taken. Please choose a different spot.")
			return None

		self.board.set_piece(row, col, self.current_player)
		if (self.check_for_win(row, col, self.current_player) == True):
			print("We have a winner!")
			self.game_started = False
		else:
			self.set_current_player(self.current_player)

	def get_current_player(self) -> pl.Player:
		return self.current_player

	def set_current_player(self, prev: pl.Player) -> None:
		self.current_player = list(self.players - {self.current_player})[0]

	def get_players(self) -> set[pl.Player]:
		return self.players

	def view_board(self) -> None:
		print(self.board)

	### Private functions go here ###

	# TODO
	def __check_board_horizontal(self, row: int, player: pl.Player) -> bool:
		winning_placement = np.full(shape = (1, 4), fill_value = player.get_piece().name, dtype = str)
		# Check against row for match against mission placement.
		return False

	# TODO
	def __check_board_vertical(self, col: int, player: pl.Player) -> bool:
		return False

	# TODO
	def __check_board_diagonal_left(self, row: int, col: int, player: pl.Player) -> bool:
		return False

	# TODO
	def __check_board_diagonal_right(self, row: int, col: int, player: pl.Player) -> bool:
		return False

	### End of Private funcitons ###
	def check_for_win(self, row: int, col: int, player: pl.Player) -> bool:
		return (self.__check_board_horizontal(row, player) and self.__check_board_vertical(col, player) and
				self.__check_board_diagonal_left(row, col, player) and self.__check_board_diagonal_right(row, col, player))


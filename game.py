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
		self.board.clear_board()
		self.game_started = True
		self.current_player = self.player_1
		print("Time to start the game! Player_1 will start.")

	def __validate_placement(self, row: int, col: int) -> bool:
		if (self.game_started == False):
			print("Game has not started. Please start game before setting pieces.")
			return False
		
		if (self.board.get_piece(row, col) != "*"):
			print("Board slot is taken. Please choose a different spot.")
			return False

		if (row < (self.board.row_length - 1) and self.board.get_piece(row + 1, col) == "*"):
			print("Place piece at the lowest available row of that column.")
			return False
		return True

	def set_piece(self, row: int, col: int) -> None:
		if (self.__validate_placement(row, col) == False):
			return None

		self.board.set_piece(row, col, self.current_player)
		print("Curr Player just played: " + self.current_player.__str__())
		if (self.check_for_win(row, col, self.current_player) == True):
			print(self.current_player.__str__() + " has won!")
			self.game_started = False
		else:
			self.set_current_player(self.current_player)
			print("Next Player: " + self.current_player.__str__())

	def get_current_player(self) -> pl.Player:
		return self.current_player

	def set_current_player(self, prev: pl.Player) -> None:
		self.current_player = list(self.players - {self.current_player})[0]

	def get_players(self) -> set[pl.Player]:
		return self.players

	def view_board(self) -> None:
		print(self.board)

	### Private functions go here ###
	@staticmethod
	def check_four_in_list(a: list, piece: pl.Piece) -> bool:
		winning_placement = np.full(shape = 4, fill_value = piece.name, dtype = str).tolist()
		for i in range(len(a) - len(winning_placement) + 1):
			if a[i:i+len(winning_placement)] == winning_placement:
				return True
		return False

	def __check_board_horizontal(self, row: int, col: int, player: pl.Player) -> bool:
		return Game.check_four_in_list(self.board.get_surr_row(row, col), player.get_piece())

	def __check_board_vertical(self, row: int, col: int, player: pl.Player) -> bool:
		return Game.check_four_in_list(self.board.get_surr_col(row, col), player.get_piece())

	def __check_board_diagonal_left(self, row: int, col: int, player: pl.Player) -> bool:
		return Game.check_four_in_list(self.board.get_diag_left(row, col), player.get_piece())

	def __check_board_diagonal_right(self, row: int, col: int, player: pl.Player) -> bool:
		return Game.check_four_in_list(self.board.get_diag_right(row, col), player.get_piece())

	### End of Private funcitons ###
	def check_for_win(self, row: int, col: int, player: pl.Player) -> bool:
		return (self.__check_board_horizontal(row, col, player) or self.__check_board_vertical(row, col, player) or
				self.__check_board_diagonal_left(row, col, player) or self.__check_board_diagonal_right(row, col, player))


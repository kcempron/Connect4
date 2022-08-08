from enum import Enum

# Piece Enum to fix Board Piece Options
class Piece(Enum):
	X = 1
	O = 2

# Provides information about the player within the game.
class Player:
	def __init__(self, piece: Piece) -> None:
		self.piece = piece

	def get_piece(self) -> Piece:
		return self.piece

	def __str__(self) -> str:
		return "Player Piece: " + self.piece.name

import game as g
import player as pl
import board as b

if __name__ == "__main__":
	# Test Basic Functionality of class Player
	player1 = pl.Player(pl.Piece.X)
	player2 = pl.Player(pl.Piece.O)
	print(player1)
	print(player2)

	# Test Basic Functionality of class Board
	board = b.Board(4, 4)
	print(board)
	board.set_piece(3, 0, player1)
	print(board)
	board.set_piece(3, 1, player2)
	print(board)
	board.clear_board()
	print(board)

	# Test Basic Functionality of class Game
	game = g.Game(4, 4, pl.Piece.X, pl.Piece.O)
	game.start_game()
	game.view_board()
	game.set_piece(3, 0)
	game.view_board()
	game.set_piece(3, 1)
	game.view_board()
	game.set_piece(3, 1)
	game.view_board()
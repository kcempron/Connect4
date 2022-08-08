import game as g
import player as pl
import board as b

if __name__ == "__main__":
	# Test Basic Functionality of class Board
	board = b.Board(4, 4)
	print(board)
	board.set_piece(0, 0)
	print(board)
	board.set_piece(3, 0)
	print(board)
	board.clear_board()
	print(board)
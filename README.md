# Connect 4 Design Doc

## Summary
This is a quick Coding excerise to build out the functional aspects of the game Connect 4.

## Setup
When designing a game like Connect 4, we will want to ask 3 initial questions:
- What is the state of the world of the game?
- How does the game work?
- How do you win the game?

These questions will help us dictate the different states of the game as well as the validations required
to make sure that the "win condition" is met fairly and consistently.

### The State of the World
> Connect 4 is consists of two opposing players each with a set of pieces that they can place onto a board.
> The board is usually **7 rows x 6 columns** but for the sake of this exercise, the board can be of arbitrary size.

### The Game Rules
> Each turn, a player will alternate placing one of their pieces in a given column of the board. The piece will
> occupy the first available row slot from the bottom. A player can not arbitrarily place a piece in any position
> on the board if the space is already occupied or if there are empty slots below the desired position.

### The Winner Takes it All
> The objective of the game, as the name implies, is to have the first player have 4 of their pieces on the board
> align either horizontally, vertically, or diagonally.

## Approach
When designing this game, I want to break it up into 3 main components:
### The Game:
```
# Handles the state of the game and ensures that players are able to interact with the board within constraints.

Class Game:
  def start_game()
  def reset_game()
  def set_current_piece()
  def get_current_player()
  def check_for_win()
```
### The Board:
```
# Provides the structure on which pieces are played within the constraints of the game.

Class Board:
  def create_board()
  def clear_board()
  def set_piece()
  def get_board()
  def view_board()
```

### The Player:
```
# Provides information about the player within the game.

Class Player:
  def create_player()
  def get_piece()
```

## Further Development / Desired Optimizations
- Have players just choose column to drop piece as opposed to choosing row, col.
- Have option to select who starts game.
- Create Board states for easier and faster testing
- Build more robust test suite that can also validate on assertions of game constraints.
- Expand test to validate against a wide range of board sizes.
- Have historical tracking of the game such that moves can be replayed and recreated.
- Personalize Player to track name, win history, and other meta data.

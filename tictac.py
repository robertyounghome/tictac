# author: Robert (Bob) Young
# date: 12/29/2020
# tictac.py
# A very simple game of TicTacToe in which the computer and player both move randomly.
# Output is to console.

import random

class Board:

	# Initializes the board, allows for board to be initially filled in, I use this for ease of testing
	def __init__(self, initial=None):
		k = 0
		self.board = [['.' for _ in range(3)] for _ in range(3)]
		self.open = {}
		for i in range(3):
			for j in range(3):
				if not initial or initial[k] == '.':
					self.open[(i, j)] = 1
				else:
					self.board[i][j] = initial[k]
				k += 1
		self.computer = 'X'
		self.player = 'O'
		self.outcome = ''

	# Prints the board
	def __str__(self):
		return ''.join([' '.join(self.board[i]) + "\n" for i in range(3)])

	# Randomly pick a valid move on the tictactoe board, return as tuple
	def generate_move(self):
		i = random.randint(0, len(self.open) - 1)
		move = list(self.open.keys())[i]
		del self.open[move]
		return move

	# Computer makes a move
	def computer_move(self):
		i, j = self.generate_move()
		self.board[i][j] = self.computer

	# Returns True if somebody won, otherwise False
	def checkForResult(self, s):
		if s == 'XXX':
			self.outcome = 'Computer wins!'
			return True
		elif s == 'OOO':
			self.outcome = 'Player wins!'
			return True	
		return False	

	# Checks to see if the game is over, if so, returns True, otherwise False
	def over(self):
		diagonal1 = diagonal2 = ''
		for i in range(3):
			# horizontal or vertical
			if self.checkForResult(''.join(self.board[i])) or self.checkForResult(''.join([self.board[j][i] for j in range(3)])):
				return True
			# set up for diagonals
			diagonal1 += self.board[i][i]
			diagonal2 += self.board[i][2 - i]
		# diagonals
		if self.checkForResult(diagonal1) or self.checkForResult(diagonal2):
			return True
		# Tie Game
		if not self.open:
			self.outcome = 'Tie Game!'
			return True
		return False

	# The player makes a move
	def player_move(self):
		i, j = self.generate_move()
		self.board[i][j] = self.player	

# Will create the board and play a game of TicTacToe one time.
# Results of each move are outputed to the console.
if __name__ == '__main__':
	game = Board()
	print(game)
	for i in range(9):
		if i % 2 == 0:
			game.computer_move()
		else:
			game.player_move()
		print(game)
		if game.over():
			break
	print(game.outcome)
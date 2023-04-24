import random
class Tiktaktoe:
	def __init__(self,player,opponent):
		self.template = {}
		self.frow = []
		self.player_score = 0
		self.opponent_score = 0
		self.player = player
		self.opponent = opponent


	def tut_maps(self):
		self.frow = [i for i in range(1,10)]
		self.template = dict(enumerate(self.frow,1))

	def maps(self):
		self.frow = [i for i in range(1,10)]
		self.template = dict(enumerate(self.frow,1))
		print(f'player1: {self.player_score}, opponent: {self.opponent_score}')

	def maps_editor(self,turns,symbol):
		if self.template[turns] == 'X' or self.template[turns] == 'O':
			print('That spot has already been played')
			pass
		else:
			self.template[turns] = symbol

	def X_win(self):
		print(self.player,' wins')
		self.player_score += 1
		self.maps()

	def O_win(self):
		print(self.opponent,' wins')
		self.opponent_score += 1
		self.maps()

	def board_printer(self):
		c1 = 0
		c2 = 1
		c3 = 2
		ph = list(self.template)
		for v in range(3):
			print('\n\n', ' '*10,self.template[ph[c1]]," " * 7,self.template[ph[c2]]," " * 7,self.template[ph[c3]] )
			c1 += 3
			c2 += 3
			c3 += 3
		# Horizontal strike for first row
		if (self.template[1] == 'X' ) and (self.template[2] == 'X') and (self.template[3] == 'X' ):
			self.X_win()
		# Horizontal strike for second row
		elif (self.template[4] == 'X' ) and (self.template[5] == 'X') and (self.template[6] == 'X') :
			self.X_win()
		# Horizontal strike for third row
		elif (self.template[7] == 'X' ) and (self.template[8] == 'X') and (self.template[9] == 'X'):
			self.X_win()
		# Vertical strike for first column
		elif (self.template[1] == 'X' ) and (self.template[4] == 'X') and (self.template[7] == 'X') :
			self.X_win()
		# Vertical strike for second column
		elif (self.template[2] == 'X' ) and (self.template[5] == 'X') and (self.template[8] == 'X'):	
			self.X_win()
		# Vertical strike for third column
		elif (self.template[3] == 'X' ) and (self.template[6] == 'X') and (self.template[9] == 'X'):	
			self.X_win()
		# First strike for leading diagonal
		elif (self.template[1] == 'X' ) and (self.template[5] == 'X') and (self.template[9] == 'X'):	
			self.X_win()
		# Second strike for ladding diagonal
		elif (self.template[3] == 'X' ) and (self.template[5] == 'X') and (self.template[7] == 'X'):
			self.X_win()
		# Horizontal strike for first row
		elif (self.template[1] == 'O' ) and (self.template[2] == 'O') and (self.template[3] == 'O' ):
			self.O_win()
		# Horizontal strike for second row
		elif (self.template[4] == 'O' ) and (self.template[5] == 'O') and (self.template[6] == 'O') :
			self.O_win()
		# Horizontal strike for third row
		elif (self.template[7] == 'O' ) and (self.template[8] == 'O') and (self.template[9] == 'O'):
			self.O_win()
		# Vertical strike for first column
		elif (self.template[1] == 'O' ) and (self.template[4] == 'O') and (self.template[7] == 'O') :
			self.O_win()
		# Vertical strike for second column
		elif (self.template[2] == 'O' ) and (self.template[5] == 'O') and (self.template[8] == 'O'):	
			self.O_win()
		# Vertical strike for third column
		elif (self.template[3] == 'O' ) and (self.template[6] == 'O') and (self.template[9] == 'O'):	
			self.O_win()
		# First strike for leading diagonal
		elif (self.template[1] == 'O' ) and (self.template[5] == 'O') and (self.template[9] == 'O'):	
			self.O_win()
		# Second strike for ladding diagonal
		elif (self.template[3] == 'O' ) and (self.template[5] == 'O') and (self.template[7] == 'O'):
			self.O_win()

	def wins(self):
		if self.player_score > self.opponent_score:
			print(self.player,' wins!')
		elif self.player_score < self.opponent_score:
			print(self.opponent,' wins!')
		elif self.player_score == self.opponent_score:
			print("It's a tie!")

player1 = input('Please type your name as player 1: ')
opponent = input('Please type your name as Opponent: ')
sample = Tiktaktoe(player1,opponent)
sample.tut_maps()
sample.board_printer()
print('''\n\nThe first tile on the upper left can be accessed by pressing 1, and so on and so forth.
Make a sequence of X or O pattern, either horizontally, vertically or diagonally.''')
sample.maps()

while True:
	player_score = 0
	opponent_score = 0
	X_turn = int(input(f"\nIt's {player1} turn to make a move. Please select a position to place X on the board: "))
	if X_turn == 0:

		break
	sample.maps_editor(X_turn,'X')
	sample.board_printer()
	O_turn = int(input(f"\nIt's {opponent} turn to make a move. Please select a position to place O on the board: "))
	if O_turn == 0:
		break
	sample.maps_editor(O_turn,'O')
	sample.board_printer()	
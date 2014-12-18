# Tic Tac Toe game to be played in the Terminal

# contains entire game; set up and run
def run_game():
	# individual cell values
	cell = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

	# printable board
	board = '\n\t ' + cell[0] + ' | ' + cell[1] + ' | ' + cell[2] + '\n\t-----------\n\t ' + cell[3] + ' | ' + cell[4] + ' | ' + cell[5] + '\n\t-----------\n\t ' + cell[6] + ' | ' + cell[7] + ' | ' + cell[8]


	# determines whether O (player 1) has 3 in a row 
	def o_wins(cell): 
	    if (cell[0] == cell[1] == cell[2] == 'O' or cell[3] == cell[4] == cell[5] == 'O' or cell[6] == cell[7] == cell[8] == 'O' 
	    	or cell[0] == cell[3] == cell[6] == 'O' or cell[1] == cell[4] == cell[7] == 'O' or cell[2] == cell[5] == cell[8]== 'O'
			or cell[0] == cell[4] == cell[8] == 'O' or cell[2] == cell[4] == cell[6] == 'O'):
	    	return True
	    return False

	# determines whether X (player 2) has 3 in a row 
	def x_wins(cell):
	    if (cell[0] == cell[1] == cell[2] == 'X' or cell[3] == cell[4] == cell[5] == 'X' or cell[6] == cell[7] == cell[8] == 'X' 
	    	or cell[0] == cell[3] == cell[6] == 'X' or cell[1] == cell[4] == cell[7] == 'X' or cell[2] == cell[5] == cell[8]== 'X'
	    	or cell[0] == cell[4] == cell[8] == 'X' or cell[2] == cell[4] == cell[6] == 'X'):
	        return True
	    return False

	# if board is filled and noone has won, return true
	def tie(cell):
	    if (cell[0] in ('O', 'X') and cell[1] in ('O', 'X') and cell[2] in ('O', 'X') and cell[3] in ('O', 'X') and cell[4] in ('O', 'X') 
	    	and cell[5] in ('O', 'X') and cell[6] in ('O', 'X') and cell[7] in ('O', 'X') and cell[8] in ('O', 'X')):
	        return True
	    return False

	# check if selection is a valid position (1-9)
	def pos_check(zmove):
	        try:
	        	move_test = int(zmove)
	        	if move_test in range(1,10):
	        		return True
	        	return False
	        except ValueError:
	        	return False


	# title page
	print('\n\n \t TIC TAC TOE \n') 


	# game setup
	instructions = input('Would you like to read the instructions? (y/n)') 
	if instructions == 'y':
	    print('\n Players take turns to place a peice on the following grid:\n\n\t 1 | 2 | 3\n\t-----------\n\t 4 | 5 | 6\n\t-----------\n\t 7 | 8 | 9\n\nInput a position when prompted. The first player to have 3 peices in a row wins.')
	player1 = input('Enter player 1\'s name: ')
	player2 = input('Enter player 2\'s name: ')
	print(player1 + ', you are O and ' + player2 + ', you are X.')
	nextPlayer = player1	


	# begin game loop
	while not tie(cell) and not (o_wins(cell) or x_wins(cell)):
		print('\n\nThis is the board:\n' + board)
		move = input('\n' + nextPlayer + ', select a number (1 - 9) to place your peice: ')
		while not pos_check(move):
			move = input('Invalid position. Please select again:')
		if nextPlayer == player1:
			cell[int(move) - 1] = 'O' # off by one indexing
			board = '\n\t ' + cell[0] + ' | ' + cell[1] + ' | ' + cell[2] + '\n\t-----------\n\t ' + cell[3] + ' | ' + cell[4] + ' | ' + cell[5] + '\n\t-----------\n\t ' + cell[6] + ' | ' + cell[7] + ' | ' + cell[8]
			nextPlayer = player2
		else:
			cell[int(move) - 1] = 'X' # off by one indexing
			board = '\n\t ' + cell[0] + ' | ' + cell[1] + ' | ' + cell[2] + '\n\t-----------\n\t ' + cell[3] + ' | ' + cell[4] + ' | ' + cell[5] + '\n\t-----------\n\t ' + cell[6] + ' | ' + cell[7] + ' | ' + cell[8]
			nextPlayer = player1


	# display appropriate end-game result
	if o_wins(cell):
	    print('\nCongratulations ' + player1 + ', you are the winner!')
	elif x_wins(cell):
	    print('\nCongratulations ' + player2 + ', you are the winner!')
	else:
	    print('\nIt is a tie.. Better luck next time!')

# runs as many games as desired
again = 'y'
while again == 'y':
	run_game()
	again = input('\nWould you like to play again? (y/n)')
input('Press <enter> to quit.')
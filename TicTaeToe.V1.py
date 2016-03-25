# TicTacToe Project

board = [ str(number) for number in range(1,10) ]
draw = False
player_one_symbol_const = "X"
player_two_symbol_const = "O"

def printBoard():
	global board
	string =  "\t" + "   |   |   \n"
	string += "\t" + " " + board[0] + " | " + board[1] + " | "+ board[2] + " \n"
	string += "\t" + "___|___|___\n"
	string += "\t" + "   |   |   \n"
	string += "\t" + " " + board[3] + " | " + board[4] + " | "+ board[5] + " \n"
	string += "\t" + "___|___|___\n"
	string += "\t" + "   |   |   \n"
	string += "\t" + " " + board[6] + " | " + board[7] + " | "+ board[8] + " \n"
	print string

def loadMove(player, input):
	global board
	global draw
	global player_one_symbol_const
	global player_two_symbol_const

	if board[input-1] == str(input):
		board[input-1] = player
	else:
		return -1 # Wrong move

	#Check column
	if input % 3 == 0:
		column = 3
	else:
		column = input % 3

	if board[column-1] == board[column-1+3] == board[column-1+6] == player:
		return player

	#Check row
	if input in range(1,4):
		if board[0] == board[1] == board[2] == player:
			return player
	elif input in range(4,7):
		if board[3] == board[4] == board[5] == player:
			return player
	elif input in range(7,10):
		if board[6] == board[7] == board[8] == player:
			return player

	#Check Diagons
	if board[0] == board[4] == board[8] == player:
		return player

	if board[6] == board[4] == board[2] == player:
		return player

	lista = [ item for item in board if item not in  [player_one_symbol_const, player_two_symbol_const] ]

	if len(lista) == 0:
		draw = True


next = player_one_symbol_const
clearWindow = True

while not draw:
	if clearWindow:
		print chr(27) + "[2J"
		print "Welcome to my TicTacToe project\n"
		printBoard()

	clearWindow = True
	print "Please enter a number from 1 to 9\n"
	if next == player_one_symbol_const:
		input = raw_input("What is your move Player 1?\n")
	else:
		input = raw_input("What is your move Player 2?\n")

	if input not in [str(number) for number in range(1,10)]:
		print "You must input a number between 1..9"
		clearWindow = False
		continue

	status = loadMove(next, int(input))
	if status == -1:
		print "Wrong Move"
	elif status == player_one_symbol_const:
		printBoard()
		print "Player 1 won the match"
		exit()
	elif status == player_two_symbol_const:
		printBoard()
		print "Player 2 won the match"
		exit()
	else:
		if next == player_one_symbol_const:
			next = player_two_symbol_const
		else:
			next = player_one_symbol_const

print "DRAW! Match is over."	
# TicTacToe Project Version 2

board = [[1,2,3],[4,5,6],[7,8,9]]

draw = False
player_one_symbol_const = "X"
player_two_symbol_const = "O"

def printBoard():
	global board
	string =  "\t" + "   |   |   \n"
	string += "\t" + " " + str(board[0][0]) + " | " + str(board[0][1]) + " | "+ str(board[0][2]) + " \n"
	string += "\t" + "___|___|___\n"
	string += "\t" + "   |   |   \n"
	string += "\t" + " " + str(board[1][0]) + " | " + str(board[1][1]) + " | "+ str(board[1][2]) + " \n"
	string += "\t" + "___|___|___\n"
	string += "\t" + "   |   |   \n"
	string += "\t" + " " + str(board[2][0]) + " | " + str(board[2][1]) + " | "+ str(board[2][2]) + " \n"
	print string


def loadMove(player, input):
	global board
	global draw
	global player_one_symbol_const
	global player_two_symbol_const

	#Check column
	if input % 3 == 0:
		column = 2
	else:
		column = input % 3 - 1

	#Check row
	if input % 3 == 0:
		row = input / 3 - 1
	else:
		row = input / 3

	if board[row][column] == input:
		board[row][column] = player
		
	for i in range(0,3):
		if board[row][i] != player:
			break
		elif i == 2:
			return player

	for i in range(0,3):
		if board[i][column] != player:
			break
		elif i == 2:
			return player

	#Check Diagons
	if board[0][0] == board[1][1] == board[2][2] == player:
		return player

	if board[0][2] == board[1][1] == board[2][0] == player:
		return player

	lista = [ item for item in board if item not in  [player_one_symbol_const, player_two_symbol_const] ]

	if len(lista) == 0:
		draw = True

	pass


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
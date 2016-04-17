import random

deck = []
suits = ['Heart', 'Diamond', 'Spade', 'Club' ]

class Player(object):
	
	# Attributes
	# name = Player Name
	# amount = Amount of money the player has for bet

	def __init__(self,name,amount=1000):
		self.name = name
		self.amount = amount
		self.cards = []

	def win(self, bet):
		self.amount += bet

	def lost(self, bet):
		self.amount -= bet

	def addCard(self, card):
		self.cards.append(card)

	def clean(self):
		del self.cards[:]

	def getAmountCards(self):
		return len(self.cards)

	def getValue(self):
		# Fix issue: 1 + 7 + 5
		value = 0
		numbers = [ x.number for x in self.cards ]

		for card in sorted(numbers, reverse=True):
			if card >= 10:
				value += 10
			elif card == 1:
				if value+11 > 21:
					value += 1
				else:
					value += 11
			else:
				value += card

		return value

class Card(object):
	# Attributes
	def __init__(self, suit, number):
		self.suit = suit
		self.number = number

	def __str__(self):
		return self.suit + " " + str(self.number)

def ShuffleCards():
	global suits
	global deck
	random.seed()
	_deck = set()
	del deck[:]
	while True:
		if len(_deck) == 52:
			break
		_deck.add((suits[random.randint(0,3)],random.randint(1,13)))

	for item in _deck:
		deck.append(Card(item[0],item[1]))

	random.shuffle(deck)

def clearWindow():
	print chr(27) + "[2J"
	print "Welcome to my BlackJack project\n"

def play(player, bet):
	global deck

	while True:
		aCard = deck.pop()
		player.addCard(aCard)
		print "Here is card: " + str(aCard)
		print "Total hand: " + str(player.getValue())
		if player.getAmountCards() == 2 and player.getValue() == 21:
			print "BlackJack Natural"
			break
		if player.getValue() > 21:
			print "Lost"
			player.lost(bet)
			return
		if player.getValue() == 21:
			break

		answer = raw_input("Hit or Run?\n") 
		if answer[0] == 'r' or answer[0] == 'R':
			break
	
	print "Now it's my turn"
	dealer = Player("Dealer",0)

	while True:
		aCard = deck.pop()
		dealer.addCard(aCard)
		print "Here is card: " + str(aCard)
		print "Total hand: " + str(dealer.getValue())
		if dealer.getAmountCards() == 2 and dealer.getValue() == 21:
			print "BlackJack Natural"
			print "You Lost"
			player.lost(bet)
			break
		elif dealer.getValue() > 21:
			print "You win"
			player.win(bet)
			break
		elif dealer.getValue() >= player.getValue():
			print "You Lost"
			player.lost(bet)
			break


def main():
	global deck
	ShuffleCards()
	clearWindow()
	name = raw_input("What is your name Player?\n")
	amount = float(raw_input("How much money do you have for bet?\n"))
	bet = float(raw_input("How much money do you want to bet?\n"))
	player = Player(name,amount)
	while True:
		ShuffleCards()
		play(player, bet)
		player.clean()
		print "Stats: "
		print "Player: " + player.name
		print "Money: " + str(player.amount)
		if player.amount < bet:
			print "You are out of money"
			break
		answer = raw_input("Do you want to continue?\n")
		if answer[0] == 'n' or answer[0] == 'N':
			break


main()
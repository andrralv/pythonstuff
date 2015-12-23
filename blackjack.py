# Blackjack game
# From 1 to 7 players compete against a dealer
# 12/21/15

import cards, games

class BJ_Card(cards.Card):
	"""A blackjack Card"""
	ACE_VALUE = 1

	def get_value(self):
		if self.is_face_up:
			value = BJ_Card.RANKS.index(self.rank) + 1
			if value > 10:
				value = 10
		else:
			value = None 
		return value
	value = property(get_value)

class BJ_Deck(cards.Deck):
	"""A blackjack deck"""
	def populate(self):
		for suit in BJ_Card.SUITS:
			for rank in BJ_Card.RANKS:
				self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
	"""A blackjack hand"""
	def __init__(self, name):
		super(BJ_Hand, self).__init__()
		self.name = name
	def __str__(self):
		rep = self.name + "\t" + super(BJ_Hand, self).__str__()
		if self.total:
			rep += "(" + str(self.total) + ")"
		return rep
	def get_total(self):
		"""if a card has no value, total is None"""
		for card in self.cards:
			if not card.value:
				return None
		#add up card values, treat aces as 1
		total = 0
		for card in self.cards:
			total += card.value

		#determine if hand contains Ace
		contains_ace = False
		for card in self.cards:
			if card.value == BJ_Card.ACE_VALUE:
				contains_ace = True

		#if hand contains Ace and total is low enough, treat ace as 11
		if contains_ace and total <= 11:
			#add only 10 since we're already added 1 for the ace
			total += 10

		return total
	total = property(get_total)

	def is_busted(self):
		return self.total > 21

class BJ_Player(BJ_Hand):
	"""A blackjack player"""
	def is_hitting(self):
		response = games.ask_yes_no("\n" + self.name + ", do you want a hit? y/n: ")
		return response == 'y'
	def bust(self):
		print self.name, "busts."
		self.lose()
	def lose(self):
		print self.name, "loses."
	def win(self):
		print self.name, "wins."
	def push(self):
		print self.name, "pushes."

class BJ_Dealer(BJ_Hand):
	"""A blackjack dealer"""
	def is_hitting(self):
		return self.total < 17
	def bust(self):
		print self.name, "busts."
	def flip_first_card(self):
		first_card = self.cards[0]
		first_card.flip()

class BJ_Game(object):
	"""A blackjack game"""
	def __init__(self, names):
		self.players = []
		for name in names:
			player = BJ_Player(name)
			self.players.append(player)

		self.dealer = BJ_Dealer("Dealer")

		self.deck = BJ_Deck()
		self.deck.populate()
		self.deck.shuffle()

	def get_still_playing(self):
		remaining = []
		for player in self.players:
			if not player.is_busted():
				remaining.append(player)
		return remaining

	# list of players still playing (not busted) this round
	still_playing = property(get_still_playing)

	def __additional_cards(self, player):
		while not player.is_busted() and player.is_hitting():
			self.deck.deal([player])
			print player
			if player.is_busted():
				player.bust()

	def play(self):
		#deal initial 2 cards to everyone
		self.deck.deal(self.players + [self.dealer], per_hand = 2)
		self.dealer.flip_first_card()	#hide dealers first card
		for player in self.players:
			print player
		print self.dealer

		#deal additional cards to players
		for player in self.players:
			self.__additional_cards(player)

		self.dealer.flip_first_card() # reveal dealers first
 		if not self.still_playing:
 			# since all players have busted, just show the dealers hand
 			print self.dealer
 		else:
 			# deal additional cards to dealer
 			print self.dealer
 			self.__additional_cards(self.dealer)

 			if self.dealer.is_busted():
 				#everyone still playing wins
 				for player in self.still_playing:
 					player.win()
 			else:
 				#compare each player still playing to dealer
 				for player in self.still_playing:
 					if player.total > self.dealer.total:
 						player.win()
 					elif player.total < self.dealer.total:
 						player.lose()
 					else:
 						player.push()
 		#remove everyones cards
 		for player in self.players:
 			player.clear()
 			self.dealer.clear()


def main():
	print "\t\tWelcome to Blackjack!\n"

	names = []
	number = games.ask_number("How many players? (1-7): ", low = 1, high = 8)
	for i in range(number):
		name = raw_input("Enter the player's name: ")
		names.append(name)
	print 

	game = BJ_Game(names)

	again = None
	while again != "n":
		game.play()
		again = games.ask_yes_no("\nDo you want to play again?: ")


main()
raw_input("\n\nPress the enter key to exit. ")



#games module
#basic classes for questions in a game
#12/21/15

class Player(object):
	"""A player for a game"""
	def __init__(self, name, score = 0):
		self.name = name
		self.score = score

	def __str__(self):
		rep = self.name + ":\t" + str(self.score)
		return rep

def ask_yes_no(question):
	response = None
	while response not in ("y", "n"):
		response = raw_input(question).lower()
	return response

def ask_number(question, low, high):
	"""ask for a number within a range"""
	response = None
	while response not in range(low, high):
		response = int(raw_input(question))
	return response

if __name__ == "__main__":
	print "You ran this module directly, this is supposed to be imported"
	raw_input("\n\npress any key to exit")
	
# movie chooser 2.0
# uses radio buttons instead
# 12/28/15

from Tkinter import *

class Application(Frame):
	"""A GUI app to pick a fave movie"""
	def __init__(self, master):
		"""Initialize frame"""
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
	def create_widgets(self):
		"""create widgets for movie choices"""
		#create description label
		Label(self,
	 		text = "Choose your favorite type of movie: ").grid(row = 0, column = 0, sticky = W)
	 		#create instruction label
	 	Label(self, 
	 		text = "Select one: "
	 		).grid(row = 1, column = 0, sticky = W)
	 	#create a variable for a single, favorite movie type
	 	self.favorite = StringVar()

	 	#create comedy radio button
	 	Radiobutton(self, 
	 		text = "comedy",
	 		variable = self.favorite,
	 		value = "comedy",
	 		command = self.update_text,
	 		).grid(row = 2, column = 0, sticky = W)

	 	#create drama radio button
	 	Radiobutton(self, 
	 		text = "drama",
	 		variable = self.favorite,
	 		value = "drama",
	 		command = self.update_text,
	 		).grid(row = 3, column = 0, sticky = W)

	 	#create romance radio button
	 	Radiobutton(self, 
	 		text = "romance",
	 		variable = self.favorite,
	 		value = "romance",
	 		command = self.update_text,
	 		).grid(row = 4, column = 0, sticky = W)

	 	#create text field to display result
	 	self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
	 	self.results_txt.grid(row = 5, column = 0, columnspan = 3)

	def update_text(self):
		"""update text field and display users favorite picks"""
		message = "Your favorite movie type is "
		message += self.favorite.get()
		self.results_txt.delete(0.0, END)
		self.results_txt.insert(0.0, message)

#main
root = Tk()
root.title("Movie Chooser 2")
app = Application(root)
root.mainloop()

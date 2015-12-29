# Movie Chooser
# Here comes the choo choo train
# 12/27/15

from Tkinter import *

class Application(Frame):
	"""A GUI app for choosing favorite movie types"""
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create widgets for movie choices"""
		Label(self,
			text = "Choose your favorite movie types"
			).grid(row = 0, column = 0, sticky = W)
		Label(self, 
			text = "Select all that apply:"
			).grid(row = 1, column = 0, sticky = W)
		#create comedy check button
		self.likes_comedy = BooleanVar()
		Checkbutton(self,
			text = "comedy",
			variable = self.likes_comedy,
			command = self.update_text,
			).grid(row =2, column = 0, sticky = W)
		#create drama check button
		self.likes_drama = BooleanVar()
		Checkbutton(self,
			text = "drama",
			variable = self.likes_drama,
			command = self.update_text,
			).grid(row =3, column = 0, sticky = W)
		#create drama button
		self.likes_romance = BooleanVar()
		Checkbutton(self,
			text = "romance",
			variable = self.likes_romance,
			command = self.update_text,
			).grid(row =4, column = 0, sticky = W)
		#create text field to display results
		self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
		self.results_txt.grid(row = 5, column = 0, columnspan = 3)
	def update_text(self):
		"""update text widget and display users favorites movie types"""
		likes = ""

		if self.likes_comedy.get():
			likes += "You like comedy gold, lel.\n"
		if self.likes_drama.get():
			likes += "You are a drama queen, kek.\n" 
		if self.likes_romance.get():
			likes += "You can into bromance as well.\n" 
		self.results_txt.delete(0.0, END)
		self.results_txt.insert(0.0, likes)

#main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()




# lazy buttons 2
# demonstrates using a class with Tkinter
# 24/12/15

from Tkinter import *

class Application(Frame):
	"""A GUI application with three buttons"""
	def.__init__(self, master):
		"""Initialize the frame"""
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create three buttons that didn do nuffin"""
		# create first button
		self.bttn1 = Button(self, text = "I didn do nuffin")
		self.bttn1.grid()

		# create second button
		self.bttn2 = Button(self)
		self.bttn2.grid()
		self.bttn2.configure(text = "Me neither!")

		# create third button
		self.bttn3 = BUtton(self)
		self.bttn3 = grid()
		self.btt3["text"] = "Same here!"

# main 
root = Tk()
root.title("Lazy buttons 2")
root.geometry("200x85")

app = Application(root)

root.mainloop()


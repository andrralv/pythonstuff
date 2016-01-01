# click counter
# it counts my clicks, if you know what i mean
# 24/12/15

from Tkinter import *

class Application(Frame):
	"""A GUI application that counts button clicks"""
	def __init__(self, master):
		"""initialize the frame"""
		Frame.__init__(self, master)
		self.grid()
		self.bttn_clicks = 0 # number of button clicks
		self.create_widget()

	def create_widget(self):
		""" Create button which displays number of clicks. """
		self.bttn = Button(self)
		self.bttn["text"] = "Total Clicks: 0"
		self.bttn["command"] = self.update_count
		self.bttn.grid()

	def update_count(self):
		""" Increase click count and display new total """
		self.bttn_clicks += 1
		self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

# main 

root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()








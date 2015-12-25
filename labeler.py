# Labeler
# Demonstrates a label
# 12/24/15

from Tkinter import *

# create the root window
root = Tk()
root.title("Labeler")
root.geometry("200x50")

app = Frame(root)
app.grid()

lbl = Label(app, text = "I'm a label!")
lbl.grid()

#kick off the windows event loop
root.mainloop()



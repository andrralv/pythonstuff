# Lazy buttons
# they din do nuffin
# 24/12/15

from Tkinter import *

# create a root window
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

# create a frame in the window to hold other widgets

app = Frame(root)
app.grid()

btt1 = Button(app, text = "I didn do nuffin")
btt1.grid()

btt2 = Button(app)
btt2.grid()
btt2.configure(text = "Me neither!")

btt3 = Button(app)
btt3.grid()
btt3["text"] = "Same here!"

#kick off the windows event loop
root.mainloop()




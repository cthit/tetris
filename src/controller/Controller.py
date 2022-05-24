import tkinter as tk


class Controller:

	def key(self,event):
		print("Key: ", event.char)
	def __init__(self):
		self.root = tk.Tk()
		self.root.bind_all("<Key>", self.key)
	def run(self):
		self.root.mainloop()
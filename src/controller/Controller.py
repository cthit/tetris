import tkinter as tk
from model.Model import Model


class Controller:

	def key(self,event):
		print("Key: ", event.char)
		self.model.update(event.char)
	def __init__(self,model):
		self.root = tk.Tk()
		self.root.bind_all("<Key>", self.key)
		self.model=model
	def run(self):
		self.root.mainloop()
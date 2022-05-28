import keyboard
from model.Model import Model
from controller.Observer import Observer

#Legacy maybe, probably don't use
class Controller(Observer):

	def __init__(self,updateable):
		self.updateable=updateable
		print("Initialized controller")
	def update(self):
		if keyboard.read_key()!=None:
			return None